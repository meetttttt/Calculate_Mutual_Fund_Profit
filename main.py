import uuid
import utils
import logging

from datetime import datetime
from fastapi import FastAPI, HTTPException

# Initialize the FastAPI
app = FastAPI()

# Configure logging with timestamp
logging.basicConfig(filename="logs.log",
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@app.get("/home")
async def testing_route():
    logging.info("Testing_route called")
    return {"message": "Hello World"}


@app.get("/profit/")
def calculate_profit_route(scheme_code: str,
                           start_date: str,
                           end_date: str,
                           capital: float = 1000000.0):
    try:
        # Generate a UUID
        request_id = uuid.uuid4()

        # Log a message with the UUID
        logging.info(f"Request {request_id}: Starting processing...")
        logging.info(f"Scheme: {scheme_code}, Start Date: {start_date}, End Date: {end_date}, Capital: {capital}")

        # Validate start_date and end_date
        if not utils.validate_date(start_date) or not utils.validate_date(end_date):
            logging.info(f"Start Date and End Date not in correct format.")
            raise HTTPException(status_code=422, detail="Invalid date format. Please use DD-MM-YYYY")

        start_date = datetime.strptime(start_date, '%d-%m-%Y')
        end_date = datetime.strptime(end_date, '%d-%m-%Y')

        # Check if start_date is smaller than end_date
        if start_date > end_date:
            logging.info(f"Start Date > End Date not in correct format.")
            raise HTTPException(status_code=422, detail="Start date must be smaller than end date.")

        logging.info(f"Start Date and End Date in correct format.")

        # Calculating the profit
        success, profit = utils.calculate_profit(scheme_code,
                                                 start_date,
                                                 end_date,
                                                 capital)
        # Checking for errors
        if not success:
            logging.info(f"Request {request_id}: Ended with Error: {profit}")
            raise HTTPException(status_code=422, detail=profit)
        else:
            # Returning the profit made
            logging.info(f"Request {request_id}: Ended Successfully.")
            return {"profit": profit}

    except Exception as e:  # General Error Handling
        logging.error(e)
        raise HTTPException(status_code=400, detail=str(e))
