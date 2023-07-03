drinks = ['coffee', 'soda', 'tea']
dinner = ['chicken', 'beef', 'veggies']
dessert = ['cake', 'candy']

# print list all grouped together
food = [drinks, dinner, dessert]
print(food)
    # [
        # ['coffee', 'soda', 'tea'], ['chicken', 'beef', 'veggies'], ['cake', 'candy']
    # ]
    
# this will access the list in given index
print(food[0])
    # ['coffee', 'soda', 'tea']

# to acess one elem in the list, use a second set of [] and list the index of the elem
print(food[0][0])
    # coffee
    
# this will access dinner list or index 1 list and the value in index 2 of that list
print(food[1][2])
    # veggies

# this will acess dessert list receive an error, there is no elem at index 
print([2][2])
    # IndexError: list index out of range