# set
utensils = {'fork', 'spoon', 'knife'}

# display all of the values
for i in utensils:
#     # when printed all of the elem found within utensils, if you run again they might be in a different order
    print(i)
#     # spoon         fork        knife
#     # fork          knife       fork
#     # knife         spoon       spoon

# set is faster than a list if you need to check to see if something is within a set compared to a list and they do not allow any duplicate values




# # only one 'knife' value is printed
utensils = {'fork', 'spoon', 'knife', 'knife', 'knife'}
for x in utensils:
    print(x)
    # spoon
    # knife
    # fork


# useful methods of sets

utensils = {'fork', 'spoon', 'knife'}

# add given value to end of list (version 1)
utensils.add('napkin')
print(utensils)
    # {'spoon', 'fork', 'napkin', 'knife'}

# or

# add given value to end of list
utensils.add('taco')
for i in utensils:
    print(i)
    # spoon
    # fork
    # knife
    # taco
    # napkin
    
# remove given value
utensils.remove('spoon')
for i in utensils:
    print(i)
    # knife
    # fork
    
# all the elem in our set should be gone
utensils.clear('spoon')
for i in utensils:
    print(i)
    
# second set 
utensils = {'fork', 'spoon', 'knife'}
dishes = {'plate', 'cup', 'bowl'}

# update method, add one set to another
utensils.update(dishes)        # utensils.update(dishes)
for i in utensils:
    print(i)
    # plate                     # cup
    # bowl                      # fork
    # cup                       # spoon
    # spoon                     # knife
    # knife                     # plate
    # fork                      # bowl
    
# join method to sets together and create two sets entirely
dinner_table = utensils.union(dishes)
for i in dinner_table:  
    print(i)
    # fork              
    # cup
    # bowl
    # plate
    # spoon
    # knife
    
# or

# without for loop
dinner_table = utensils.union(dishes)
print(dinner_table)
    # # {'knife', 'spoon', 'fork', 'cup', 'bowl', 'plate'}
    
# compare similarities and differences in sets
utensils = {'fork', 'spoon', 'knife'}
# add knife to dishes set
dishes = {'plate', 'cup', 'bowl', 'knife'}
# what does utensils have that dishes doesnt
print(utensils.difference(dishes))
    # {'fork', 'spoon'}
# ^ ⌄ they both have knives so that's why knife isn't appearing
print(dishes.difference(utensils))
    # {'plate', 'cup', 'bowl'}
    
# intersection method check if sets have anything in common -- returns only what they have in common
print(utensils.intersection(dishes))
    #{'knife'}