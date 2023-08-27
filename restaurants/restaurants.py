#!/usr/bin/env python3
class Review:

    all_reviews = []

    def __init__(self, customer: str, restaurant: str, rating: int):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating

        # Append each instance into all_reviews list 
        Review.all_reviews.append(self)
        Restaurant.restaurant_customers.add(self._customer)




    def rating(self):
        return self._rating
    
    def customer(self):
        return self._customer
    
    def restaurant(self):
        return self._restaurant
    

    # Getters and setters for the customer object
    # Once a review is created, should not be able to change the customer

    def get_customer(self):
        return self._customer
    
    def set_customer(self, customer):
        return self._customer
    
    customer_name = property(get_customer, set_customer)



    # Getters and setters for the restaurant object
    # Once a review is created, should not be able to change the customer

    def get_restaurant(self):
        return self._restaurant
    
    def set_restaurant(self, restaurant):
        return self._restaurant
    
    restaurant_name = property(get_restaurant, set_restaurant)


    @classmethod
    def all(cls):
        return f"All reviews: {', '.join({str(review) for review in cls.all_reviews})}" # using a set so there's no duplication of reviews

    def __str__(self):
        return f'{self._customer} for {self._restaurant}: {self._rating} stars'
    

''' RESTAURANT CLASS'''

class Restaurant:

    all_restaurants = []
    restaurant_customers = set()

    def __init__(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            print("Name must be a string.")

        self._reviews = []


       # Add all restaurant instances to 'all_restaurants'
        Restaurant.all_restaurants.append(self)


    def reviews(self):
        return [review.rating() for review in self._reviews]
        # return f"Reviews for {self.name} restaurant: {', '.join([str(review.rating()) for review in self._reviews])}"


    # Getters and setters for the name
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        return self._name
    
    name = property(get_name, set_name)

    def customers(self):
        customer_set = {review.customer() for review in self._reviews if review.restaurant() == self.name}
        for review in Review.all_reviews:
            if review.restaurant() == self.name:
                customer_set.add(review.customer())
        return customer_set


    
''' CUSTOMER CLASS'''

class Customer:

    all_customers = []

    def __init__(self, first_name: str, last_name: str):
        if isinstance(first_name, str) and isinstance(last_name, str):
            self._first_name = first_name
            self._last_name = last_name
        else:
            print("All names must be a string.")
            self._first_name = ""
            self._last_name = ""

        # Add reviews for each customer instance
        self._reviews = []

        # Once created, append the instance to 'all_customers'
        Customer.all_customers.append(self)

    def given_name(self):
        return self._first_name
    
    def family_name(self):
        return self._last_name

    def full_name(self):
        self.customer_full_name = f'{self._first_name} {self._last_name}'
        return self.customer_full_name

    # Getters and setters for the first name
    def get_given_name(self):
        return self._first_name
    
    def set_given_name(self, first_name):
        if isinstance(first_name, str):
            self._first_name = first_name
        else:
            print(f"Failed to set {first_name} as first name. First name must be a string.")
    
    first_name = property(get_given_name, set_given_name)

    # Getters and setters for the last name

    def get_family_name(self):
        return self._last_name
    
    def set_family_name(self, last_name):
        if isinstance(last_name, str):
            self._last_name = last_name
        else:
            print(f"Failed to set {last_name} as last name. Last name must be a string.")
    
    last_name = property(get_family_name, set_family_name)

    # Get all of the customer instances
    # Defining a class method that returns the list of all customer instances in all_customers list.

    @classmethod
    def all(cls):
        return cls.all_customers

    # Using __repr__() method to return a string representation of the object
        
    def __repr__(self):
        # return f"Customer('{self.first_name}', '{self.last_name}')"
        return self.full_name()
    
    # Adding customer reviews - create review instances for each
    def add_review(self, restaurant: Restaurant, rating: int):
        review = Review(self.full_name(), restaurant.name, rating)  # Use self.full_name() instead of self
        self._reviews.append(review)
        restaurant._reviews.append(review)
        # restaurant.restaurant_customers.add(review)


    def reviews(self):
        customer_review_rep = [f"{review._restaurant} - {review.rating()} stars" for review in self._reviews]
        return f"Reviews by {self.full_name()}: {', '.join(customer_review_rep)}"
    
    
# customer_1 = Customer("John", "Doe")
# customer_2 = Customer("Bill", "Gates")
# customer_3 = Customer("Weird", "Person")
# customer_4 = Customer("Forky", "Biscuit")
# customer_5 = Customer("Anne", "Kiguta")
# customer_6 = Customer("Wes", "Snipes")
# print(customer.family_name())
# # print(customer.full_name())
# # customer.first_name = "Jane"
# # print(customer.given_name())
# customer.last_name = "Smith"
# print(customer.family_name())

# print(Customer.all())

# restaurant1 = Restaurant("Highlands")
# restaurant1.name = "Azuri"
# print(restaurant1.name)

# review1 = Review("John Doe", "Highlands", 5)
# review2 = Review("John Doe", "abc", 3)
# review3 = Review("John Doe", "xyz", 2)
# review4 = Review("John Doe", "CJs", 5)
# print(Review.all())


# print(review1.rating())

# More >>
# Create customers
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

# Create reviews
review1 = Review("John Doe", "Highlands", 3)
review2 = Review("Mike Posner", "Azuri", 5)
review3 = Review("Travis Scott", "Pwani Dishes", 4)
review4 = Review("Jane Doe", "Kilimanjaro Jamia", 5)
review5 = Review("Ed Sheeran", "Highlands", 4)
review6 = Review("Ed Sheeran", "Highlands", 4)


# Create restaurants
restaurant1 = Restaurant("Highlands")
restaurant2 = Restaurant("Kilimanjaro Jamia")

# Add reviews
customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 6)

print(customer1.reviews())
print(review1.customer())
print(review1.restaurant())
print(restaurant1.reviews())
print(Review.all())
print(restaurant1.customers())