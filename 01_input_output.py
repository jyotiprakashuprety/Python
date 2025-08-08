# Ask the user for their name and age, then print: "Hello John! You are 25 years old."

name = input("Enter your Name:")

while True:
    age = input("Enter your age:")
    if age.isdigit():
        age = int(age)
        if 0<= age <= 120:
            break
        else:
            print("Age must be between 0 to 120")
    else:
        print("Please enter the valid age!")
print(f"Hello {name}! You are {age} years old")


# Convert a number of minutes given by the user into hours and minutes (e.g., 130 minutes → 2 hours and 10 minutes).


# Take two numbers as input, and print their sum, difference, product, and quotient.

# Ask for a string and print it in uppercase, lowercase, and title case.

# Ask for a word and print how many letters it has.