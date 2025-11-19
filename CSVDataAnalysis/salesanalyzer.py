import pandas as pd 
from typing import Dict, List 

class SalesAnalyzer:
    """
    performs analysis on sales data from sales csv file.
    uses pandas groupby, lanbda filters and aggregation functions.
    """

    def __init__(self, csv_file_path: str):
        self.df = pd.read_csv(csv_file_path) 
    
    def total_sales_per_category(self) -> Dict[str, float]:
        """
        calculate total sales per category.
        """
        return (
            self.df.assign(TotalSales=lambda x: x['UnitsSold'] * x['UnitPrice'])
            .groupby('Category')['TotalSales']
            .sum()
            .sort_values(ascending=False)
            .to_dict()
        )
    
    def total_sales_by_region(self) -> Dict[str, float]:
        """
        calculate total sales by region.
        """
        return (
            self.df.assign(TotalSales=lambda x: x['UnitsSold'] * x['UnitPrice'])
            .groupby('Region')['TotalSales']
            .sum()
            .sort_values(ascending=False)
            .to_dict()
        )

    def average_transaction_value(self) -> float:
        """
        calculate average transaction value.
        """
        self.df['TotalSales'] = self.df['UnitsSold'] * self.df['UnitPrice']
        return self.df['TotalSales'].mean() 

    def top_n_orders(self, n: int) -> List[Dict]:
        """
        get top n orders by total sales.
        """
        self.df['TotalSales'] = self.df['UnitsSold'] * self.df['UnitPrice']
        top_orders = (
            self.df.sort_values(by='TotalSales', ascending=False)
            .head(n)
            .to_dict(orient='records')
        )
        return top_orders
    
    def orders_over_threshold(self, threshold: float) -> pd.DataFrame:
        """
        filter orders with total sales over a certain threshold.
        """
        self.df['TotalSales'] = self.df['UnitsSold'] * self.df['UnitPrice']
        filtered_orders = self.df[self.df['TotalSales'] > threshold]
        return filtered_orders.to_dict(orient='records')