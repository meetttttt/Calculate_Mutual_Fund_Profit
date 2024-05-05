# Mutual Fund Profit Calculator

- This Python project calculates the profit for a mutual fund investment based on the Net Asset Value (NAV) data obtained from an API.
- The user will provide the start date, end date, and capital invested to calculate the profit for the mutual fund investment.

## Features

- Calculate profit for a mutual fund investment based on NAV data.
- Handle missing dates in the NAV data.

## Requirements

- Python 3.x
- FastAPI library
- Requests library

## Installation

1. Clone the repository -> Install Requirements -> Run FastAPI:

```bash
git clone https://github.com/your-username/mutual-fund-profit-calculator.git
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
fastapi dev main.py
```

# Request URL:
```
GET http://127.0.0.1:8000/profit?scheme_code=101206&start_date=26-07-2023&end_date=18-10-2023&capital=1000000.0
```

# Curl:
```
curl -X 'GET' \
  'http://127.0.0.1:8000/profit/?scheme_code=101206&start_date=10-12-2020&end_date=25-09-2023&capital=1000000' \
  -H 'accept: application/json'
```

# Docs
![image](https://github.com/meetttttt/Calculate_Mutual_Fund_Profit/assets/74391584/acd7b3ff-ea84-4f15-bd68-96cdf1bb4646)

# API Endpoint
The FastAPI app exposes the following endpoint:
- /home: Testing route to check whether endpoint is working or not.
- /profit: Calculates the profit for a mutual fund investment based on provided parameters.
