# input("What is your name? ") # terminal will show input and you can type your name "Poh" -- then press enter -- program done running

# name = input("What is your name? ")

# print("Hello " + name) # Hello Dale 
# What is your name? 
# Enter a name -- Dale-- press enter

# age = input("How old are you? ")
# # age = age + 1 # TypeError: can only concatenate str (not "int") to str

# age = int(input("How old are you? ")) # 12
# age = age + 1 # still does not add age but no error

# print("Hello " + name)
# print("You are " + age + " years old") # TypeError: can only concatenate str (not "int") to str

# print("You are " + str(age) + " years old") # You are 13 years old
# age = 10.2 -- ValueError: invalid literal for int() with base 10: '10.2'


name = input("What is your name? ") # Dale
age = int(input("How old are you? ")) # 34
height = float(input("How tall are you? ")) # 69.1
age = age + 1
print("Hello " + name) # Hello Dale
print("You are " + str(age) + " years old") # You are 35 years old
print("You are " + str(height) + "cm tall") # You are 69.1cm tall