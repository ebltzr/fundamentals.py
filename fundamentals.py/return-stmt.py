# print the value that is calling the multiply function 
def multiply(num1, num2):
    result = num1 * num2
    return result

print(multiply(6,8))
    # 48

# store the return value within a variable
def multiply(num1, num2):
    result = num1 * num2
    return result

x = multiply(6,8)

print(x)
    # 48
    
# shorter code with no variable same result
def multiply(num1, num2):
    return num1 * num2

x = multiply(6,8)

print(x)