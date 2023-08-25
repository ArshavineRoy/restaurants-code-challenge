#!/usr/bin/env python3

from restaurants import Customer, Restaurant, Review
import io
import sys

class TestRestaurantReviewSystem:
    '''Restaurant, Customer, and Review in restaurants.py'''

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
        customer.given_name("Jane")
        assert customer.given_name() == "Jane"

    def test_family_name_change(self):
        '''should be able to change the family name after creation'''
        customer = Customer("John", "Doe")
        customer.family_name("Smith")
        assert customer.family_name() == "Smith"

    def test_all_customers(self):
        '''returns all of the customer instances'''
        Customer._all = []
        customer1 = Customer("John", "Doe")
        customer2 = Customer("Jane", "Smith")
        assert Customer.all() == [customer1, customer2]
