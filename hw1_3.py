import unittest

# 攝氏轉華氏的函數
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 單元測試類別
class TestTemperatureConversion(unittest.TestCase):

    # 測試零度轉換
    def test_zero_celsius(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)
    
    # 測試正值轉換
    def test_positive_celsius(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        self.assertEqual(celsius_to_fahrenheit(37), 98.6)
    
    # 測試負值轉換
    def test_negative_celsius(self):
        self.assertEqual(celsius_to_fahrenheit(-40), -40)
    
    # 測試小數點值
    def test_decimal_celsius(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(36.6), 97.88, places=2)

# 運行測試
if __name__ == '__main__':
    unittest.main()