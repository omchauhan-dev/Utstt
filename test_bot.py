
import unittest
from fare_calculator import get_fare_and_validity
from station_data import get_distance
from bot import get_train_type

class TestBot(unittest.TestCase):

    def test_get_fare_and_validity(self):
        # Test case 1: Short distance
        fare, validity = get_fare_and_validity(45)
        self.assertEqual(fare, 25)
        self.assertEqual(validity, "3 hours")

        # Test case 2: Medium distance
        fare, validity = get_fare_and_validity(200)
        self.assertEqual(fare, 85)
        self.assertEqual(validity, "24 hours")

        # Test case 3: Long distance
        fare, validity = get_fare_and_validity(1500)
        self.assertEqual(fare, 460)
        self.assertEqual(validity, "24 hours")

    def test_get_distance(self):
        # Test case 1: Known route
        distance = get_distance("mumbai", "delhi")
        self.assertEqual(distance, 1384)

        # Test case 2: Unknown route
        distance = get_distance("mumbai", "goa")
        self.assertIsNone(distance)

    def test_get_train_type(self):
        # Test case 1: Short distance
        train_type = get_train_type(50)
        self.assertEqual(train_type, "Local / MEMU")

        # Test case 2: Long distance
        train_type = get_train_type(500)
        self.assertEqual(train_type, "Passenger")

if __name__ == '__main__':
    unittest.main()
