#!/usr/bin/env python3
class Restaurant:
    def __init__(self):
        pass
    

class Customer:
    def __init__(self, first_name, last_name):
        if isinstance(first_name, str) or isinstance(last_name, str ):
            self.first_name = first_name
            self.last_name = last_name
        else:
            return "All names must be a string."

    def given_name(self):
        return self.first_name
    
class Review:
    def __init__(self):
        pass


customer = Customer("John", "Doe")
print(customer.given_name())