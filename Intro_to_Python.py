# Intro-to-python-assignment
    #My Intro to Python assignment for practicing variables, arithmetic, strings, and data types.
""
#Part 1: Variables and Data Types
""
# Assigning different types of values to variables
name = "UGOwealth"         # string
""
age = 45                  # integer
""
height = 5.73             # float
""
is_student = True         # boolean
""
""
# Showing variable values and their data types
print("Name:", name, "| Data type:", type(name))
print("Age:", age, "| Data type:", type(age))
print("Height:", str(height) + " ft", "| Data type:", type(height))
print("Is Student:", is_student, "| Data type:", type(is_student))

""
""
""
""
""
# Part 2: Arithmetic Operations
""
# Basic arithmetic
a = 46
b = 5
""
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus (Remainder):", a % b)
print("Exponentiation:", a ** b)
""
""
""
""
""
# Part 3: String Operations
""
# Working with strings
greeting = "Hello"
subject = "Delta_Nigeria"
""
""
# Concatenation
message = greeting + " " + subject
print("Concatenated String:", message)
""
""
# Repetition
print("Repetition:", subject * 3)
""
""
# String formatting (f-string)
print(f"My name is {name} and I am {age} years old.")
""
""
""
""
""
# Part 4: User Input
""
# Collecting user input
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
""
print(f"Hello, {user_name}! You are {user_age} years old.")
