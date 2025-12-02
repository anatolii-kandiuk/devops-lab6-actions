import unittest
from calculator import WeightConverter


class TestWeightConverter(unittest.TestCase):
    
    def setUp(self):
        self.converter = WeightConverter()
    
    def test_grams_to_kilograms(self):
        self.assertEqual(self.converter.grams_to_kilograms(1000), 1.0)
        self.assertEqual(self.converter.grams_to_kilograms(5000), 5.0)
        self.assertEqual(self.converter.grams_to_kilograms(500), 0.5)
    
    def test_grams_to_tonnes(self):
        self.assertEqual(self.converter.grams_to_tonnes(1000000), 1.0)
        self.assertEqual(self.converter.grams_to_tonnes(500000), 0.5)
        self.assertEqual(self.converter.grams_to_tonnes(2000000), 2.0)
    
    def test_kilograms_to_grams(self):
        self.assertEqual(self.converter.kilograms_to_grams(1), 1000)
        self.assertEqual(self.converter.kilograms_to_grams(5), 5000)
        self.assertEqual(self.converter.kilograms_to_grams(0.5), 500)
    
    def test_kilograms_to_tonnes(self):
        self.assertEqual(self.converter.kilograms_to_tonnes(1000), 1.0)
        self.assertEqual(self.converter.kilograms_to_tonnes(500), 0.5)
        self.assertEqual(self.converter.kilograms_to_tonnes(2000), 2.0)
    
    def test_tonnes_to_grams(self):
        self.assertEqual(self.converter.tonnes_to_grams(1), 1000000)
        self.assertEqual(self.converter.tonnes_to_grams(0.5), 500000)
        self.assertEqual(self.converter.tonnes_to_grams(2), 2000000)
    
    def test_tonnes_to_kilograms(self):
        self.assertEqual(self.converter.tonnes_to_kilograms(1), 1000)
        self.assertEqual(self.converter.tonnes_to_kilograms(0.5), 500)
        self.assertEqual(self.converter.tonnes_to_kilograms(2), 2000)
    
    def test_zero_values(self):
        self.assertEqual(self.converter.grams_to_kilograms(0), 0)
        self.assertEqual(self.converter.kilograms_to_grams(0), 0)
        self.assertEqual(self.converter.tonnes_to_kilograms(0), 0)
    
    def test_conversion_chain(self):
        original = 1500
        kg = self.converter.grams_to_kilograms(original)
        back_to_grams = self.converter.kilograms_to_grams(kg)
        self.assertEqual(original, back_to_grams)


if __name__ == "__main__":
    unittest.main()
