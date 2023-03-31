from django.test.testcases import TestCase

from src.apps.user.models import UserAddress, Customer


class UserAddressModelTest(TestCase):
    def setUp(self) -> None:
        self.customer = Customer(username="test")
        self.user_address = UserAddress.objects.create(
            address_1="Test1", address_2="Test2", city="SomeCity", postal_code=2020, county=None
        )
        self.customer.address = self.user_address

    def test_str(self):
        self.assertEqual(
            f"Customer {str(self.customer.username)}'s addresses", str(self.user_address)
        )
