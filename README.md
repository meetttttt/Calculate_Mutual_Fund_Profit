# Mutual Fund Profit Calculator

- This Python project calculates the profit for a mutual fund investment based on the Net Asset Value (NAV) data obtained from an API. 

## Features

- Calculate profit for a mutual fund investment based on NAV data.
- Handle missing dates in the NAV data.

## Requirements

- Python 3.x
- FastAPI
- Requests library

## Installation

1. Clone the repository -> Install Requirements -> Run FastAPI:

```bash
git clone https://github.com/your-username/mutual-fund-profit-calculator.git
cd mutual-fund-profit-calculator
pip install -r requirements.txt
fastapi dev main.py
```

# Example Request
```
GET /profit?scheme_code=101206&start_date=26-07-2023&end_date=18-10-2023&capital=1000000.0
```

# Docs
![image](https://github.com/meetttttt/Calculate_Mutual_Fund_Profit/assets/74391584/acd7b3ff-ea84-4f15-bd68-96cdf1bb4646)

# API Endpoint
The FastAPI app exposes the following endpoint:

- /profit: Calculates the profit for a mutual fund investment based on provided parameters.
