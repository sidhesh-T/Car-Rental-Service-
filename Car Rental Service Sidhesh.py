#!/usr/bin/env python
# coding: utf-8

# # Car Rental Service

# In[2]:


from enum import Enum
from datetime import datetime


class CarCategory(Enum):
    COMPACT = 1
    PREMIUM = 2
    MINIVAN = 3
    


class RentalCarAdmin:
    def __init__(self, base_day_rental, kilometer_price):
        self.base_day_rental = base_day_rental
        self.kilometer_price = kilometer_price
        self.bookings = {}
        
        

    def register_rental(self, booking_number, customer_name, car_category, rental_time, mileage):
        if booking_number in self.bookings:
            return "Booking number already exists. Please provide a unique booking number."

        self.bookings[booking_number] = {
            "customer_name": customer_name,
            "car_category": car_category,
            "rental_time": rental_time,
            "mileage": mileage,
        }
        return "Rental registration successful."
    
    

    def calculate_price(self, booking_number, return_time, current_mileage):
        if booking_number not in self.bookings:
            return "Invalid booking number. Please provide a valid booking number."

        rental_info = self.bookings[booking_number]
        category = rental_info["car_category"]
        rental_time = rental_info["rental_time"]
        mileage = rental_info["mileage"]
        number_of_days = (return_time - rental_time).days
        number_of_kilometers = current_mileage - mileage

        if category == CarCategory.COMPACT:
            price = self.base_day_rental * number_of_days
        elif category == CarCategory.PREMIUM:
            price = self.base_day_rental * number_of_days * 1.2 + self.kilometer_price * number_of_kilometers
        elif category == CarCategory.MINIVAN:
            price = self.base_day_rental * number_of_days * 1.7 + self.kilometer_price * number_of_kilometers * 1.5
        else:
            return "Invalid car category."

        return f"Price for rental period: {price:.2f} USD"

    
    

# Test cases
if __name__ == "__main__":
    base_day_rental = 50
    kilometer_price = 0.2
    rental_system = RentalCarAdmin(base_day_rental, kilometer_price)


    
    # Test Case 1: Rental registration
    response1 = rental_system.register_rental(1001, "John Doe", CarCategory.COMPACT, datetime(2023, 7, 20), 20000)
    print(response1)  # Output: Rental registration successful.


    
    # Test Case 2: Car Return and Price Calculation
    response2 = rental_system.calculate_price(1001, datetime(2023, 7, 25), 20500)
    print(response2)  # Output: Price for rental period: 250.00 USD


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




