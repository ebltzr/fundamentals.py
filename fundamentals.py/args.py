# function accepts two numbers as arguments; add them together and return the sum
def add(num1,num2):
    sum = num1 + num2
    return sum
# what if we need to pass 3 arguments bu there's only two parameters
# print(add(1,2,3))
    # TypeError: add() takes 2 positional arguments but 3 were given

# replace parameters with *args, can be named anything but has to have asterisk -- what we are doing is a form of packing, we are passing all of these arguments and packing them into a tuple
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3))
    # 6
print(add(1,2,3,8,6,3))
    # 23

# renamed *args -- still works with tuples they are ordered and unchangeable (NOT mutable)
def add(*stuff):
    sum = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3))
    # 6

# this displays error because tuples are unchangeable
def add(*stuff):
    sum = 0
    stuff[0] = 0  # <-- this causes error because you are trying to change index [0]
    for i in stuff:
        sum += i
    return sum

# print(add(1,2,3))
    # TypeError: 'tuple' object does not support item assignment

# convert tuple into different collection -- list -- one way is to cast it 
def add(*stuff):
    sum = 0
    # a list is changeable (mutable)
    stuff = list(stuff)
    stuff[0] = 0 
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3))
    # 5 --> index[0] is now 0 not 1 ; 0+2+3 = 5
