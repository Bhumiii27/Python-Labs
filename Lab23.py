#Write a code combine both validations into a single program
import re

# Function to validate PAN
def validate_pan(pan):
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    return bool(re.match(pattern, pan))

# Function to validate Email
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# Main Program
pan = input("Enter PAN Card Number: ")
email = input("Enter Email ID: ")

# Check PAN
if validate_pan(pan):
    print("PAN Card Number is Valid.")
else:
    print("PAN Card Number is Invalid.")

# Check Email
if validate_email(email):
    print("Email ID is Valid.")
else:
    print("Email ID is Invalid.")
