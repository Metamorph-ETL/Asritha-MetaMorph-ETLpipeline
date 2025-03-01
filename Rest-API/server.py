import pandas as pd
from fastapi import FastAPI,HTTPException
import os

apps = FastAPI()

# CSV File Path 
CSV_FILE_PATH = "products.csv"  

@apps.get("/products")
def get_products_from_csv():
    # Checking if file exists
    if not os.path.exists(CSV_FILE_PATH):
        raise HTTPException(status_code=404, detail="CSV file not found")
    
    # Read CSV into a DataFrame
    df = pd.read_csv(CSV_FILE_PATH)

    # Convert DataFrame to a JSON response
    return {
        "status": 200,
        "data": df.to_dict(orient="records")
    }
