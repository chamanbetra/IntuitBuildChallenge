from create_sample_csv import create_sample_csv, CSV_FILE_NAME
from salesanalyzer import SalesAnalyzer

if __name__ == "__main__":
    # Ensure sample CSV data is created
    create_sample_csv()

    analyzer = SalesAnalyzer(CSV_FILE_NAME) 

    print("\n====== SALES ANALYSIS REPORT ======\n")
    print("Total Sales per Category:")
    print(analyzer.total_sales_per_category()) 

    print("\nTotal Sales by Region:")
    print(analyzer.total_sales_by_region()) 

    print("\nAverage Transaction Value:")
    print(analyzer.average_transaction_value()) 

    print("\nTop 3 Orders by Total Sales:")
    print(analyzer.top_n_orders(3)) 

    print("\nOrders over $500")
    print(len(analyzer.orders_over_threshold(500)))