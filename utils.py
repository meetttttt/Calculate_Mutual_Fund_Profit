import requests
import logging

from typing import Any, Tuple
from datetime import datetime, timedelta

# Configure logging with timestamp
logging.basicConfig(filename="logs.log",
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def validate_date(date_str: str) -> bool:
    """
    Validate date string and return boolean value.
    :param date_str: date string to validate.
    :return: boolean value (True or False) if date string is valid date or not.
    """
    try:
        datetime.strptime(date_str, '%d-%m-%Y')
        return True
    except ValueError:  # If date not in correct order return False
        return False


def get_nav_data(scheme_code: str) -> dict:
    """
    Retrieve NAV data for a given scheme code from the API.
    :param scheme_code: The unique scheme code of the mutual fund.
    :return: Dictionary containing NAV data with dates as keys and NAV values as values.
    """
    api_url = f"https://api.mfapi.in/mf/{scheme_code}"  # API URL
    response = requests.get(api_url)  # Fetch the data
    nav_data = response.json().get('data', [])
    return {datetime.strptime(entry['date'], '%d-%m-%Y'): float(entry['nav']) for entry in nav_data}


def calculate_profit(scheme_code: str, start_date, end_date, capital: float) -> Tuple[bool, Any]:
    """
    Calculate the profit for a mutual fund investment within a specified date range.
    :param scheme_code: The unique scheme code of the mutual fund.
    :param start_date: The purchase date of the mutual fund.
    :param end_date: The redemption date of the mutual fund.
    :param capital: The initial investment amount.
    :return: Profit for the mutual fund investment.
    """
    try:

        # Retrieve NAV data
        nav_dates = get_nav_data(scheme_code)

        # Find nearest available NAV for start date
        nav_start = nav_dates.get(start_date)
        while nav_start is None and start_date <= end_date:
            start_date += timedelta(days=1)
            nav_start = nav_dates.get(start_date)

        # Find nearest available NAV for end date
        nav_end = nav_dates.get(end_date)
        while nav_end is None and end_date >= start_date:
            end_date += timedelta(days=1)
            nav_end = nav_dates.get(end_date)

        # Calculate profit
        units_allotted = capital / nav_start
        value_redemption = units_allotted * nav_end
        net_profit = value_redemption - capital

        # Log the output
        logging.info(f"Profit for {scheme_code}: {net_profit}")

        # Return the calculated net profit
        return True, net_profit

    except (KeyError, ValueError) as e:
        logging.error(e)
        return False, str(e)
