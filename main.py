import utils
import logging
from fastapi import FastAPI, HTTPException

# Initialize the FastAPI
app = FastAPI()

# Configure logging with timestamp
logging.basicConfig(filename="logs.log",
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@app.get("/home")
async def testing_route():
    return {"message": "Hello World"}


@app.get("/profit/")
def calculate_profit_route(scheme_code: str, start_date, end_date, capital: float = 100000.0):
    try:
        profit = utils.calculate_profit(scheme_code,
                                        start_date,
                                        end_date,
                                        capital)
        return {"profit": profit}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

