
# storing value (ie -2.3) within a variable called num
num= input('Enter whole positive num: ')
# convert that input to a float number because currently it is a string 
num= float(num)
# when user input is accepted find the absolute value of num
num= abs(num)
# then round to the nearest whole number
num= round(num)
# print the value
print(num)
    # input -2.3
        #output 2
        
# you can do above code with less code using nested function calls
print(round(abs(float(input('Enter whole positive num: ')))))
    # start with the innermost function (ie input) resolve that first,
    # whatever value we use as an argument to the next outermost function (ie float)
    # repeat
