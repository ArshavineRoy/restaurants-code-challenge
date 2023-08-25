#!/usr/bin/env python3
class Restaurant:
    def __init__(self):
        pass
    

class Customer:
    def __init__(self, first_name: str, last_name: str):
        if isinstance(first_name, str) and isinstance(last_name, str):
            self._first_name = first_name
            self._last_name = last_name
        else:
            print("All names must be a string.")
            self._first_name = ""
            self._last_name = ""

    def given_name(self):
        return self._first_name
    
    def family_name(self):
        return self._last_name

    def full_name(self):
        self.customer_full_name = f'{self._first_name} {self._last_name}'
        return self.customer_full_name

    def get_given_name(self):
        return self._first_name
    
    def set_given_name(self, first_name):
        if isinstance(first_name, str):
            self._first_name = first_name
        else:
            print(f"Failed to set {first_name} as first name. First name must be a string.")
    
    first_name = property(get_given_name, set_given_name)

    def get_family_name(self):
        return self._last_name
    
    def set_family_name(self, last_name):
        if isinstance(last_name, str):
            self._last_name = last_name
        else:
            print(f"Failed to set {last_name} as last name. Last name must be a string.")
    
    last_name = property(get_family_name, set_family_name)
    

class Review:
    def __init__(self):
        pass
    

# customer = Customer("John", "Doe")
# print(customer.family_name())
# # print(customer.full_name())
# # customer.first_name = "Jane"
# # print(customer.given_name())
# customer.last_name = "Lucas"
# print(customer.family_name())