import pytest
from main import calculate_profit_route


# Defining test cases using pytest's parametrize decorator
@pytest.mark.parametrize("scheme_code, start_date, end_date, capital, expected_profit", [
    ("101206", "01-01-2021", "01-01-2023", 100000.0, 7856.368043710725),
    ("101206", "01-07-2018", "01-01-2021", 333.0, 41.6868760484445),
    ("101206", "05-01-2012", "01-07-2018", 123.45, 19872.940895289612),
    ("101206", "07-01-2023", "29-01-2023", 4500, 15.654330836918234),  # start date missing
    ("101206", "08-01-2023", "28-01-2023", 50000.0, 173.93700929908664),  # end date missing
    ("101206", "08-08-2020", "23-12-2023", 5000000, 805328.3678376172),  # both the date missing
])
def test_calculate_profit(scheme_code: str, start_date: str, end_date: str,
                          capital: float, expected_profit: float) -> None:
    """
    Test function for calculate_profit_route.

    Parameters:
    - scheme_code (str): The unique scheme code of the mutual fund.
    - start_date (str): The purchase date of the mutual fund in the format 'dd-mm-yyyy'.
    - end_date (str): The redemption date of the mutual fund in the format 'dd-mm-yyyy'.
    - capital (float): The initial investment amount.
    - expected_profit (float): The expected profit for the given investment.

    Returns:
    None

    Raises:
    AssertionError: If the actual profit does not match the expected profit.
    """
    # Call the calculate_profit_route function with test inputs
    actual_result = calculate_profit_route(scheme_code, start_date, end_date, capital)

    # Check if the actual profit matches the expected profit
    assert actual_result['profit'] == expected_profit
