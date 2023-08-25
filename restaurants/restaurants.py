#!/usr/bin/env python3
class Review:
    def __init__(self):
        pass

class Restaurant:
    def __init__(self):
        pass
    

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