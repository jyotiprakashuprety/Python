# Ask the user for their name and age, then print: "Hello John! You are 25 years old."

# name = input("Enter your Name:")

# while True:
#     age = input("Enter your age:")
#     if age.isdigit():
#         age = int(age)
#         if 0<= age <= 120:
#             break
#         else:
#             print("Age must be between 0 to 120")
#     else:
#         print("Please enter the valid age!")
# print(f"Hello {name}! You are {age} years old")


# # Get input from the user
# total_minutes = int(input("Enter the number of minutes: "))

# # Calculate hours and minutes
# hours = total_minutes // 60
# minutes = total_minutes % 60

# # Display result
# print(f"{total_minutes} minutes = {hours} hour(s) and {minutes} minute(s)")


# Take two numbers as input, and print their sum, difference, product, and quotient.
num1 = int(input("Enter number 1"))
num2 = int(input("Enter number 2"))
operation = input("Enter Operation(could be "+", "-", "*", "/"):")

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    case _:
        result = "Invalid operation"

print(f"The result is : {result} ")





# Ask for a string and print it in uppercase, lowercase, and title case.

# Ask for a word and print how many letters it has.