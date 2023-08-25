#!/usr/bin/env python3

from restaurants import Customer, Restaurant, Review
import io
import sys

# Review class tests
class TestReviewClass:
    pass



# Customer class tests
class TestCustomerClass:
    '''Customer in restaurants.py'''

    def test_given_name(self):
        '''returns the customer's given name'''
        customer = Customer("John", "Doe")
        assert customer.given_name() == "John"

    def test_family_name(self):
        '''returns the customer's family name'''
        customer = Customer("John", "Doe")
        assert customer.family_name() == "Doe"

    def test_full_name(self):
        '''returns the full name of the customer'''
        customer = Customer("John", "Doe")
        assert customer.full_name() == "John Doe"

    def test_given_name_change(self):
        '''should be able to change the given name after creation'''
        customer = Customer("John", "Doe")
        customer.first_name = "Jane"
        assert customer.given_name() == "Jane"

    def test_family_name_change(self):
        '''should be able to change the family name after creation'''
        customer = Customer("John", "Doe")
        customer.last_name = "Smith"
        assert customer.family_name() == "Smith"

    def test_all_customers(self):
        '''returns all of the customer instances'''
        Customer.all_customers = []
        customer1 = Customer("John", "Doe")
        customer2 = Customer("Jane", "Smith")
        assert Customer.all() == [customer1, customer2]

# Restaurant class tests
class TestRestaurantClass:
    '''Restaurant in restaurants.py'''

    def test_initialization_with_name_arg(self):
        '''Restaurants should be initialized with a name, as a string'''
        restaurant = Restaurant("Highlands")
        assert restaurant.name == "Highlands"

    def test_name_is_a_string(self):
        '''name argument must be a string'''
        restaurant = Restaurant("Highlands")
        assert isinstance(restaurant.name, str) is True

    def test_print_if_name_not_string(self):
        '''prints "Name must be a string." if not a string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        restaurant = Restaurant(123)
        sys.stdout = sys.__stdout__
        assert (captured_out.getvalue() == "Name must be a string.\n")
        

    def test_cannot_change_restaurant_name(self):
        '''should not be able to change after the restaurant is created'''
        restaurant = Restaurant("Highlands")
        restaurant.name = "Kilimanjaro Jamia"
        assert restaurant.name == "Highlands"

