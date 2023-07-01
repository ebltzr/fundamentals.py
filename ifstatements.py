# basic form of decision making

# returns string
# age = input('How old are you? ')

# returns integer
age = int(input('How old are you? '))

# if age >= 18:
#     # indented code, block of code for that if statement
#     # if indented statement is true, execute block of code if not skip over it
#     print('You are an adult!')
        # How old are you? 18
        # You are an adult!
    # How old are you? 12 -- False
    # ((blank -- end of code ))
    
# if age >= 18:
#     print('You\'re an adult!')
#     # How old are you? 18
#         # You're an adult!
# else:
#     print('You are a child!')
#      # How old are you? 12
#         # You are a child!
        
# if age >= 18:
#     print('You are a adult!')
#     # the double equals sign is the comparison operator ( is age 100?)
#     # one equal sign is the assignment operator - python thinks you're attempting to set age to 100 not to see if age is 100
# elif age == 100:
#     print('You are century old')
# elif age < 0:
#     print('You have not been born yet')
# else:
#     print('You are a child!')

# order of if statements matter -- above code prints You are an adult when input is 100 below is corrected code


if age == 100:
    print('You are century old')
       # How old are you? 100
     # You are century old
     
elif age >= 18:
    print('You are a adult!')
       # How old are you? 35
     # You are a adult!
     
elif age <= 0:
    print('You have not been born yet')
       # How old are you? 0
     # You have not been born yet
        # How old are you? -1
     # You have not been born yet
     
else:
    print('You are a child!')
     # How old are you? 3
     # You are a adult!

     