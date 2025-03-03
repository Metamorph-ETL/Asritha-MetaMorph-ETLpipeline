
import pandas as pd
from fastapi import FastAPI, HTTPException
import os

apps = FastAPI()

# Get the absolute path of the parent directory 
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  
# Defining the path of products CSV file 
products_csv = os.path.join(base_dir, "SampleData", "products.csv")
# Defining the path of customers CSV file 
customers_csv = os.path.join(base_dir, "SampleData", "customers.csv")
# Defining the path of suppliers CSV file 
suppliers_csv = os.path.join(base_dir, "SampleData", "suppliers.csv")

@apps.get("/products")
def get_products_from_csv():
     # Checking if products file exists
    if not os.path.exists(products_csv):
        raise HTTPException(status_code=404, detail="CSV file not found")
    
    # Read CSV into a DataFrame
    df = pd.read_csv(products_csv)

    # Convert DataFrame to a JSON response
    return {
        "status": 200, 
        "data": df.to_dict(orient="records")
    }

@apps.get("/customers")
def get_customers_from_csv():
    if not os.path.exists(customers_csv):
        raise HTTPException(status_code=404, detail="customers_csv not found")
    
    df = pd.read_csv(customers_csv)

    # Droping the 'loyalty_tier' column 
    df = df.drop(columns=["loyalty_tier"]) 
    return {"status": 200, "data": df.to_dict(orient="records")}

 

@apps.get("/suppliers")  
def get_suppliers_from_csv():
    if not os.path.exists(suppliers_csv):
        raise HTTPException(status_code=404, detail="suppliers_csv not found")
    
    df = pd.read_csv(suppliers_csv)
    return {"status": 200, "data": df.to_dict(orient="records")}