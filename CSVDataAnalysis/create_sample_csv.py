
import os 

#Setup: creating CSV data for testing/demonstration 
#if no file exists, create own
CSV_CONTENT = """OrderID,Region,Category,UnitsSold,UnitPrice,SaleDate
1,East,Electronics,5,120.00,2024-01-01
2,West,Apparel,15,35.50,2024-01-01
3,South,Food,100,2.50,2024-01-02
4,East,Electronics,2,499.99,2024-01-02
5,West,Apparel,25,20.00,2024-01-03
6,North,Food,50,4.00,2024-01-03
7,North,Electronics,1,1200.00,2024-01-04
8,South,Apparel,5,80.00,2024-01-04
"""

CSV_FILE_NAME = "data/sales_data.csv"

def create_sample_csv():
    folder = os.path.dirname(CSV_FILE_NAME) 
    #Create folder if missing 
    if not os.path.exists(folder):
        print(f"Creating folder at {folder} for CSV data")
        os.makedirs(folder)

    #Create CSV file if missing
    if not os.path.exists(CSV_FILE_NAME):
        with open(CSV_FILE_NAME, 'w') as f: 
            f.write(CSV_CONTENT) 
        print(f"Created/verified sample CSV file at {CSV_FILE_NAME} for analysis")
    else:
        print(f"Sample CSV file already exists at {CSV_FILE_NAME}")

if __name__ == "__main__":
    print("Running CSV creation script...")
    create_sample_csv()