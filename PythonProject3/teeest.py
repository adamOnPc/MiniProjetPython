'''
"123".isdigit()

number = 42
text = "Hello"
decimal = 3.14

print(f"Type of {number}: {type(number)}")
print(f"Type of '{text}': {type(text)}")
print(f"Type of {decimal}: {type(decimal)}")

print("-------------------------------------------------------------------------------------------- ")

# Comparing types for validation
user_input = "25"
age = 25

print(f"user_input type: {type(user_input)}")
print(f"age type: {type(age)}")
print(f"Are they the same type? {type(user_input) == type(age)}")


print("-------------------------------------------------------------------------------------------- ")
# Comparing types for validation
user_input = "25"
age = 25

print(f"user_input type: {type(user_input)}")
print(f"age type: {type(age)}")
print(f"Are they the same type? {type(user_input) == type(age)}")

print("-------------------------------------------------------------------------------------------- ")

# Using type checking for data validation
def ageValid(age):
    if type(age) == int:
        return f"valid age : { age}"
    else :
        return f"invalid age : { age}"
print(ageValid(25))
print(ageValid(20.5))
print(ageValid("15"))

print("-------------------------------------------------------------------------------------------- ")

# Converting strings to numbers
age_str = "25"
price_str = "19.99"

# String to integer
age = int(age_str)
print(f"String '{age_str}' to int: {age}")
print(f"Type: {type(age)}")

# String to float
price = float(price_str)
print(f"String '{price_str}' to float: {price}")
print(f"Type: {type(price)}")

print("-------------------------------------------------------------------------------------------- ")

# Print function parameters
print("Line 1")
print("Line 2")
print("Line 3")

# Change the end parameter (default is newline)
print("Same line", end=" ")
print("continues here")

# Custom separator for multiple values
print("A", "B", "C", sep=" | ")
print("X", "Y", "Z", sep=" -> ")

# Redirect output (advanced)
import sys
print("Bonjour Adam", file=sys.stderr)


print("-------------------------------------------------------------------------------------------- ")


# Basic input() function usage
name = input("What is your name? ")
print(f"Hello, {name}!")

age = input("How old are you? ")
print(f"You are {age} years old")

# Note: input() always returns a string
print(f"Type of age: {type(age)}")


print("-------------------------------------------------------------------------------------------- ")


# Converting input to different types
# Getting integer input
age_str = input("Enter your age: ")
age = int(age_str)
print(f"Next year you will be {age + 1}")

# Getting float input
height_str = input("Enter your height in feet: ")
height = float(height_str)
print(f"Your height in inches: {height * 12}")

# Safe input conversion
try:
    number = int(input("Enter a number: "))
    print(f"Double of {number} is {number * 2}")
except ValueError:
    print("That's not a valid number!")

print("-------------------------------------------------------------------------------------------- ")

# Input validation examples
def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age (0-120): "))
            if 0 <= age <= 120:
                return age
            else:
                print("Age must be between 0 and 120")
        except ValueError:
            print("Please enter a valid number")

def get_yes_no(question):
    while True:
        answer = input(f"{question} (yes/no): ").lower()
        if answer in ['yes', 'y', 'no', 'n']:
            return answer in ['yes', 'y']
        print("Please answer yes or no")

# Using the validation functions
user_age = get_valid_age()
likes_python = get_yes_no("Do you like Python?")
print(f"Age: {user_age}, Likes Python: {likes_python}")

print("-------------------------------------------------------------------------------------------- ")

# Basic len() function usage
text = "Hello, World!"
numbers = [1, 2, 3, 4, 5]
student_names = ["Alice", "Bob", "Charlie"]

print(f"Length of text: {len(text)}")
print(f"Number of items in numbers: {len(numbers)}")
print(f"Number of students: {len(student_names)}")

# Length of different data types
empty_string = ""
empty_list = []
dictionary = {"name": "Alice", "age": 25}

print(f"Empty string length: {len(empty_string)}")
print(f"Empty list length: {len(empty_list)}")
print(f"Dictionary length: {len(dictionary)}")

print("-------------------------------------------------------------------------------------------- ")

# Practical uses of len()
def validate_password(password):
    if len(password) < 8:
        return "Password too short (minimum 8 characters)"
    elif len(password) > 50:
        return "Password too long (maximum 50 characters)"
    else:
        return "Password length is valid"

def count_words(sentence):
    words = sentence.split()
    return len(words)

def is_empty(data):
    return len(data) == 0

# Testing the functions
print(validate_password("123"))        # Too short
print(validate_password("mypassword123"))  # Valid
print(f"Words in sentence: {count_words('Python is awesome')}")
print(f"Is empty list empty? {is_empty([])}")


# String length operations
message = "Learning Python is fun!"

# Check string properties using len()
print(f"Message: '{message}'")
print(f"Length: {len(message)} characters")
print(f"Is short message? {len(message) < 20}")
print(f"Is long message? {len(message) > 50}")

# Working with user input length
def get_username():
    while True:
        username = input("Enter username (3-15 characters): ")
        if 3 <= len(username) <= 15:
            return username
        else:
            print(f"Username must be 3-15 characters (you entered {len(username)})")

# Truncate long strings
def truncate_text(text, max_length):
    if len(text) <= max_length:
        return text
    else:
        return text[:max_length-3] + "..."

long_text = "This is a very long text that needs to be truncated"
print(f"Original: {long_text}")
print(f"Truncated: {truncate_text(long_text, 20)}")

print("-------------------------------------------------------------------------------------------- ")

# Boolean values and operations
is_sunny = True
is_raining = False
temperature = 75

print(f"Is sunny: {is_sunny}")
print(f"Is raining: {is_raining}")
print(f"Type of is_sunny: {type(is_sunny)}")

# Boolean from comparisons
is_warm = temperature > 70
is_hot = temperature > 85
is_cold = temperature < 50

print(f"Is warm (>70°F): {is_warm}")
print(f"Is hot (>85°F): {is_hot}")
print(f"Is cold (<50°F): {is_cold}")

print("-------------------------------------------------------------------------------------------- ")

# Boolean logical operators
has_umbrella = True
is_raining = False
is_sunny = True

# AND operator - both conditions must be True
go_outside = is_sunny and not is_raining
print(f"Go outside: {go_outside}")

# OR operator - at least one condition must be True
need_protection = is_raining or (is_sunny and temperature > 90)
print(f"Need protection: {need_protection}")

# NOT operator - reverses the boolean value
stay_inside = not go_outside
print(f"Stay inside: {stay_inside}")

# Complex boolean expressions
perfect_weather = is_sunny and not is_raining and 70 <= temperature <= 80
print(f"Perfect weather: {perfect_weather}")

print("-------------------------------------------------------------------------------------------- ")

# Using any() and all() for boolean aggregation
conditions = [True, False, True]
print(f"Any true? {any(conditions)}")   # True
print(f"All true? {all(conditions)}")   # False

# Validate a password: at least one digit and one uppercase
pwd = "Pyth0nR0cks"
has_digit = any(ch.isdigit() for ch in pwd)
has_upper = any(ch.isupper() for ch in pwd)
print(f"Valid password? {has_digit and has_upper}")

print("-------------------------------------------------------------------------------------------- ")

# enumerate() adds index while iterating
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}.{fruit}")

print("-------------------------------------------------------------------------------------------- ")

# zip() pairs elements from multiple iterables

# zip() pairs elements from multiple iterables
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Use zip with different lengths (shortest wins)
a = [1,2,3]
b = [10,20]
print(list(zip(a,b)))  # [(1,10), (2,20)] '''

print("-------------------------------------------------------------------------------------------- ")

# sorted() returns a new list, list.sort() sorts in place
nums = [5, 2, 9, 1]
print(sorted(nums))        # [1, 2, 5, 9]
print(nums)                # [5, 2, 9, 1]
nums.sort()
print(nums)                # [1, 2, 5, 9]

# Custom sort with key
words = ["apple", "banana", "grape", "fig"]
print(sorted(words, key=len))  # ['fig', 'grape', 'apple', 'banana']

# reversed() returns an iterator
print(list(reversed(words)))

print("-------------------------------------------------------------------------------------------- ")

# map() transforms, filter() selects
nums = [1, 2, 3, 4]
doubles = list(map(lambda x: x*2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"doubles: {doubles}")
print(f"evens: {evens}")

# Combine with list comprehensions
squares_of_evens = [x*x for x in nums if x % 2 == 0]
print(f"squares_of_evens: {squares_of_evens}")