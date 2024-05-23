"""Tests for the Customers app"""

import json

from django.test import TestCase


TEST_CUSTOMER = {
    "first_name": "TEST",
    "last_name": "TEST",
    "address": "TEST",
    "city": "TEST",
    "zip_code": "00000",
    "state": "CO",
}


class CustomerTests(TestCase):
    """Tests for the customers app"""

    def test_duplicate(self):
        """Ensure duplicates are rejected"""
        # First case should load appropriately
        response = self.client.post("/add/", data=TEST_CUSTOMER)
        self.assertContains(
            response,
            (
                f"Added customer {TEST_CUSTOMER['first_name']} "
                f"{TEST_CUSTOMER['last_name']} successfully!"
            ),
            html=True,
        )

        # Second case should cause a failure
        response = self.client.post("/add/", data=TEST_CUSTOMER)
        self.assertContains(
            response,
            (
                "Customer with this First Name, Last Name, Street Address, "
                "City, Zip Code and State already exists."
            ),
            html=True,
        )

    def test_invalid_state(self):
        """Ensure invalid US states are rejected"""
        # Create a copy, but with an incorrect state
        invalid_customer = TEST_CUSTOMER.copy()
        invalid_customer["state"] = "NOT A STATE"
        response = self.client.post("/add/", data=invalid_customer)
        self.assertContains(
            response,
            (
                "Select a valid choice. "
                "NOT A STATE is not one of the available choices."
            ),
            html=True,
        )

    def test_invalid_zip(self):
        """Ensure invalid zip codes are rejected"""
        # Validate non-numeric zip code
        invalid_customer = TEST_CUSTOMER.copy()
        invalid_customer["zip_code"] = "bad"
        response = self.client.post("/add/", data=invalid_customer)
        self.assertContains(
            response,
            "Zip code must be numeric.",
            html=True,
        )

        # Validate zip code that is too short
        invalid_customer = TEST_CUSTOMER.copy()
        invalid_customer["zip_code"] = "1234"
        response = self.client.post("/add/", data=invalid_customer)
        self.assertContains(
            response,
            "Zip code must be 5 characters.",
            html=True,
        )

    def test_delete(self):
        """Test deletion behavior"""
        # Add the test customer
        self.client.post("/add/", data=TEST_CUSTOMER)
        delete_data = json.dumps({"customer_id": 1})

        # Delete it and check response
        response = self.client.delete("/add/", data=delete_data)
        self.assertEqual(response.content, b"1{'customers.Customer': 1}")

        # The customer should no longer exist, delete it and check response
        response = self.client.delete("/add/", data=delete_data)
        self.assertEqual(response.content, b"0{}")

    def test_get(self):
        """Check that all customers are retrieved"""
        self.client.post("/add/", data=TEST_CUSTOMER)

        customer_2 = TEST_CUSTOMER.copy()
        customer_2["first_name"] = "TEST2"
        self.client.post("/add/", data=customer_2)

        response = self.client.get("/")

        # These are stored in a div directly, so use "html=False"
        self.assertContains(response, "TEST TEST", html=False)
        self.assertContains(response, "TEST2 TEST", html=False)
