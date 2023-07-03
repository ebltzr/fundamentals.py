# name = "Taco Time"

# print(name) # make sure it is not with quotes
# print("Hello " + name) # we can combine a string (str) with another string 
# # print(type(name)) # to check datatype of variable -- <class 'str'>

# first_name = "First"
# last_name = "Last"

# # full_name = first_name + last_name
# # print("Hello " + full_name) # Hello FirstLast

# full_name = first_name + " " + last_name
# print("Hello " + full_name) # Hello First Last

# age = "21" # this would still be a string
# age = 21 # this is an int
# age = age + 1 
# print(age) # 22

# age += 1 # shortcut of age + integer
# print(age) # 22
# print(type(age)) # <class 'int'>

# age = "21"
# print(type(age)) # <class 'str'>

# age  = 21
# age += 1
# print("Your age is: " + age) # TypeError: can only concatenate str (not "int") to str

# this is typecasting -- age is now a stringn using string casting
# print("Your age is: " + str(age)) # Your age is 22

# float = floating point number (a decimal number)
    # integer (int) datatype cannot store a decimal portion - an int only stores a whole number
# height = 250.5 # floating point number - float for short
# print(height) # 250.5
# print(type(height)) # <class 'float'>
# # now create a str literal and use type casting to convert height into a str
# print("Your height is: " + str(height)) # Your height is: 250.5
# print("Your height is: " + str(height) + "cm") # Your height is: 250.5cm

# boolean -- True or False
    # variable that only stores True or False
# human = True # or False
# print(human) # True
# print(type(human)) # <class 'bool'>
# don't put boolean in quotes data type will change to str -- see that the color between str and bool changes
# human = "True"
# now what if you need to display your value along with str using str concatenation -- typecast
print("Are you a human: " + str(human)) # Are you a human: True




