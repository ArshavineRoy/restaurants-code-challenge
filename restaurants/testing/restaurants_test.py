#!/usr/bin/env python3

from restaurants import Customer, Restaurant, Review
import io
import sys

# Review class tests
class TestReviewClass:
    '''Review in restaurants.py'''
    def test_review_initialization(self):
        '''should be initialized with a customer, restaurant, and a rating (a number)'''
        review = Review("John Doe", "Highlands", 4)
        assert (review.customer() == "John Doe")
        assert (review.restaurant() == "Highlands")
        assert (review.rating() == 4)

    def test_restaurant_rating(self):
        '''returns the rating for a restaurant'''
        customer = Customer("John", "Doe")
        restaurant = Restaurant("Highlands")
        review = Review(customer, restaurant, 4)
        assert review.rating() == 4

    def test_review_all(self):
        '''returns all of the reviews'''
        Review._all = []  # Clear existing instances for the test
        customer = Customer("John", "Doe")
        restaurant = Restaurant("Highlands")
        review1 = Review("John Doe", "Highlands", 3)
        review2 = Review("Jane Doe", "Kilimanjaro Jamia", 5)
        option1 = "All reviews: Jane Doe for Kilimanjaro Jamia: 5 stars, John Doe for Highlands: 3 stars"
        option2 = "All reviews: John Doe for Highlands: 3 stars, Jane Doe for Kilimanjaro Jamia: 5 stars"
        assert Review.all() == option1 or option2

    def test_review_customer(self):
        '''returns the customer object for that review'''
        customer = Customer("John", "Doe")
        restaurant = Restaurant("Highlands")
        review = Review(customer, restaurant, 4)
        assert review.customer() == customer

    def test_review_restaurant(self):
        '''returns the restaurant object for that given review'''
        customer = Customer("John", "Doe")
        restaurant = Restaurant("Highlands")
        review = Review(customer, restaurant, 4)
        assert review.restaurant() == restaurant


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

    def test_restaurant_reviews(self):
        '''returns a list of all reviews for that restaurant'''
        customer1 = Customer("John", "Doe")
        customer2 = Customer("Jane", "Smith")
        restaurant1 = Restaurant("Highlands")
        restaurant2 = Restaurant("Kilimanjaro Jamia")
        customer1.add_review(restaurant1, 4)
        customer1.add_review(restaurant2, 5)
        customer2.add_review(restaurant1, 3)
        assert restaurant1.reviews() == [4, 3]

