# this program is for contact validation if it is valid it will print valid contact other wise they wi
# print not valid contact
import re

def is_valid_contact_number(contact_number):
    patterns = [
        r'^\d{10}$',
        r'^\d{10,11}$',                           
        r'^\d{3}-\d{3}-\d{4}$',                   
        r'^\(\d{3}\) \d{3}-\d{4}$',               
        r'^\+\d{1,3} \d{3}-\d{3}-\d{4}$',         
        r'^\d{3}[-\s]?\d{3}[-\s]?\d{4}$',         
        r'^\+(\d{2,3})-(\d{3})-(\d{3})-(\d{4})$', 
    ]
    
    for pattern in patterns:
        if re.match(pattern, contact_number):
            return True
    return False
contact_number = input("Enter a contact number: ")
if is_valid_contact_number(contact_number):
    print("Valid contact number.")
else:
    print("Invalid contact number.")
