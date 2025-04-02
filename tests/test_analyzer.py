import unittest
import pandas as pd
from src.analyzer import analyze_data

class TestAnalyzer(unittest.TestCase):
    def test_analyze_data(self):
        df = pd.DataFrame({'A': [1, 2, 3]})
        result = analyze_data(df)
        self.assertIsNotNone(result)