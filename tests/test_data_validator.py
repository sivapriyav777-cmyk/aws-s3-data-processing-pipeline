import unittest
from src.data_validator import validate_customer

class TestCustomerValidation(unittest.TestCase):

    def test_valid_customer(self):
        customer = {
            "customer_id": "101",
            "name": "John",
            "email": "john@gmail.com",
            "city": "Chennai"
        }

        self.assertTrue(validate_customer(customer))

    def test_invalid_email(self):
        customer = {
            "customer_id": "102",
            "name": "Sarah",
            "email": "invalid_email",
            "city": "Chennai"
        }

        self.assertFalse(validate_customer(customer))


if __name__ == "__main__":
    unittest.main()
