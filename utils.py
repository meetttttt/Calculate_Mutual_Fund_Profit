import requests
import logging
from datetime import datetime

# Configure logging with timestamp
logging.basicConfig(filename="logs.log",
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def calculate_profit(scheme_code: str, start_date, end_date, capital: float):
    """
    This function is define to calculate the profit of a certain scheme using a certain date range.
    :param scheme_code: The unique scheme code of the mutual fund.
    :param start_date: The purchase date of the mutual fund.
    :param end_date: The redemption date of the mutual fund.
    :param capital: The initial investment amount.
    :return: Profit for a mutual fund investment.
    """
    nav_start = None
    nav_end = None

    # Make API request to get NAV data
    api_url = f"https://api.mfapi.in/mf/{scheme_code}"
    response = requests.get(api_url)
    nav_data = response.json()

    if 'data' in nav_data:
        for entry in nav_data['data']:
            entry_date = datetime.strptime(entry['date'], '%d-%m-%Y')
            if entry_date == datetime.strptime(start_date, '%d-%m-%Y'):
                nav_start = float(entry['nav'])
            if entry_date == datetime.strptime(end_date, '%d-%m-%Y'):
                nav_end = float(entry['nav'])

    if nav_start is None:
        raise ValueError(f"NAV data not found for start date: {start_date}")
    if nav_end is None:
        raise ValueError(f"NAV data not found for end date: {end_date}")

    # Calculate number of units allotted
    units_allotted = capital / nav_start

    # Calculate value of units on redemption date
    value_redemption = units_allotted * nav_end

    # Calculate net profit
    net_profit = value_redemption - capital

    # Logging the output
    logging.info(f"Profit for {scheme_code}: {net_profit}")

    # Returning the profit made
    return net_profit


# Example usage
try:
    profit = calculate_profit(scheme_code="101206", start_date="26-07-2023", end_date="18-10-2023", capital=1000000.0)
    print(f"Net Profit: ₹{profit:.2f}")
except ValueError as e:
    print(e)
