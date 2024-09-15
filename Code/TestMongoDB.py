import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Adjust the URI as needed
db = client['Test_import_data']  # Replace with your database name

# List of CSV files and their corresponding collection names
files = {
    'X:\SIC-VN-Temp\D\Dataset_cleaned\_Users.csv': 'users',
    'X:\SIC-VN-Temp\D\Dataset_cleaned\Products.csv': 'products',
    'X:\SIC-VN-Temp\D\Dataset_cleaned\Orders.csv': 'orders',
    'X:\SIC-VN-Temp\D\Dataset_cleaned\Order_Items.csv': 'order_items',
    'X:\SIC-VN-Temp\D\Dataset_cleaned\Inventory_Item.csv': 'inventory_items',
    'X:\SIC-VN-Temp\D\Dataset_cleaned\Event.csv': 'events'
}

# Loop through the files and import them
for file_name, collection_name in files.items():
    # Read the CSV file
    df = pd.read_csv(file_name)
    # Convert DataFrame to a list of dictionaries
    data = df.to_dict(orient='records')
    # Insert data into the MongoDB collection
    db[collection_name].insert_many(data)
print("Data imported successfully!")