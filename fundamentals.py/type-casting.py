
x = 1 # int
y = 2.0 # float
z = "3" # str

print(x) # 1
print(y) # 2.0
print(z) # 3

print(int(y)) # 2

y = int(y)
print(y) # 2 -- printing variable without type cast

print(z*3) #333 -- because z is a str it will print 3 3x not multiply 3*3

z = int(z) # type cast z as an int
print(z*3) # 9

# x = float(x)
# y = float(y)
# z = float(z)
# print(x) # 1.0
# print(y) # 2.0
# print(z) # 3.0
# print(z*3) # 9.0

x = str(x)
y = str(y)
z = str(z)

print(x) # 1
print(y) # 2
print(z) # 3
print(z*3) # 333



#example for when you would need to type cast

x = 1
y = 2.0
z = "3"

# print("x is " + x) # TypeError: can only concatenate str (not "int") to str
# print("y is " + y) # TypeError: can only concatenate str (not "float") to str
print("z is " + z) # z is 3
print("x is " + str(x)) # x is 1
print("y is " + str(y)) # y is 2.0





