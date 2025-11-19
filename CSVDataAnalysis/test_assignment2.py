import unittest 
from create_sample_csv import create_sample_csv, CSV_FILE_NAME
from salesanalyzer import SalesAnalyzer 

class TestSalesAnalyzer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create sample CSV data before running tests
        create_sample_csv()
        cls.analyzer = SalesAnalyzer(CSV_FILE_NAME)
        cls.df = cls.analyzer.df

    def test_total_sales_per_category(self):
        result = self.analyzer.total_sales_per_category() 
        self.assertIsInstance(result, dict) 
        self.assertGreater(len(result), 0) 
        #ensure descending 
        values = list(result.values()) 
        self.assertGreaterEqual(values[0], values[-1]) 
    
    def test_total_sales_by_region(self):
        result = self.analyzer.total_sales_by_region() 
        self.assertIsInstance(result, dict) 
        self.assertGreater(len(result), 0) 
        #ensure descending 
        values = list(result.values())
        self.assertGreaterEqual(values[0], values[-1]) 
    
    def test_average_transaction_value(self): 
        avg = self.analyzer.average_transaction_value() 
        self.assertIsInstance(avg, float)
        self.assertGreater(avg, 0)
    
    def test_top_n_orders(self): 
        top_orders = self.analyzer.top_n_orders(3) 
        self.assertEqual(len(top_orders), 3) 
        #check descending order 
        self.assertGreaterEqual(top_orders[0]['TotalSales'], top_orders[-1]['TotalSales'])
    
    def test_orders_over_threshold(self): 
        orders = self.analyzer.orders_over_threshold(500) 
        self.assertIsInstance(orders, list) 
        for order in orders:
            self.assertGreater(order['TotalSales'], 500) 

    def test_zero_threshold_returns_all(self):
        orders = self.analyzer.orders_over_threshold(0)
        self.assertEqual(len(orders), len(self.df))

    def test_high_threshold_returns_none(self):
        orders = self.analyzer.orders_over_threshold(999999)
        self.assertEqual(len(orders), 0)

    def test_no_exceptions(self):
        try:
            self.analyzer.total_sales_per_category()
            self.analyzer.total_sales_by_region()
            self.analyzer.average_transaction_value()
            self.analyzer.top_n_orders(3)
            self.analyzer.orders_over_threshold(100)
        except Exception as e:
            self.fail(f"Method raised exception: {e}")
if __name__ == '__main__':
    unittest.main()
    
