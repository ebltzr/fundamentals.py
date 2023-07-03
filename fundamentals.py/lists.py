
# food = 'pizza' -- variable

food = ['pizza'] # list
food = ['pizza', 'ham', 'berries', 'kiwi'] # list with multiple values
print (food)
    # ['pizza', 'ham', 'berries', 'kiwi']
    
# print list given index
print(food[0])
print(food[3])
    # pizza
    # kiwi
    
# change index in list to different value
food[0] = 'taco'
print(food[0])
    # taco
    

# print list, with updated value (taco)
for x in food:
    print(x)
    # taco
    # ham
    # berries
    # kiwi
    
# append value (ice cream) to end of list
food.append('ice cream')
for x in food:
    print(x)
    # pizza
    # ham
    # berries
    # kiwi
    # ice cream

# remove value (ham) from list
food.remove('ham')
for x in food:
    print(x)
    # pizza
    # berries
    # kiwi
    
# pop will remove the last value of list
food.pop()
for x in food:
    print(x)
    # pizza
    # ham
    # berries
    
# insert will add value to given index
food.insert(0, 'cake')
for x in food:
    print(x)
    # cake
    # pizza
    # ham
    # berries
    # kiwi
    
# sort, sorts the list alphabetically
food.sort()
for x in food:
    print(x)
    # berries
    # ham
    # kiwi
    # pizza
    
# clear, clears all the elements of a list, so this will not print anything
food.clear()
for x in food:
    print(x)
