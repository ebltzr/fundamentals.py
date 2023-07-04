
student = ('Hey', 3, 'male')

# functions related to tuple, access by typing in variable. will show count and index

# count
print(student.count('Hey'))
    # 1

# index
print(student.index('male'))
    # 2
    
# you can display all of the contents of a tuple in a for loop, this will iterate once through all the values found within our tuple
for i in student:
    print(i)
    # Hey
    # 3
    # male

if 'Hey' in student:
    print('string is here')
        # string is here