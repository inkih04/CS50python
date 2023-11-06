from validator_collection import validators, checkers, errors
gmail = input("What's your email address? ")
try:
    email_address = validators.email(gmail)
except ValueError:
    print("Invalid")
else:
    print("Valid")