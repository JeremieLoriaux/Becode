import re
password = input("Enter your password :")
pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[$#@]).{6,}$"

while not re.match(pattern, password):
    print("Not a valid password please try again...")
    password = input("Enter your password :")

print("Congrats you have entered a valid password")