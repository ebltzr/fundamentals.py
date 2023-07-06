# animal = 'turtle'
# item =  'sea'

# print('The '+animal+' lives in the '+item)
#     # The turtle lives in the sea
    
# print('The {} lives in the {}'.format('turtle','sea'))
#     # The turtle lives in the sea

# print('The {} lives in the {}'.format(animal,item))
#     # The turtle lives in the sea

# # order of format field value/variable matters
# print('The {} lives in the {}'.format(item,animal))
#     # The sea lives in the turtle

# # positional argument -- using index to assign format field
# print('The {1} lives in the {0}'.format(item,animal))
#     # The turtle lives in the sea

# # ***************

# # no longer need global variables

# # keyword argument -- keyword name= value
# print('The {animal} lives in the {item}'.format(animal='turtle',item='sea'))
#     # The turtle lives in the sea
# # order of value inside braces {} does not matter
# print('The {item} lives in the {animal}'.format(animal='turtle',item='sea'))
#     # The sea lives in the turtle
# # can use the same value, and 
# print('The {animal} lives in the {animal}'.format(animal='turtle',item='sea'))
#     # The turtle lives in the turtle
# # can also use do this with the same index when working with positional arguments
# # print('The {1} lives in the {1}'.format(animal='turtle',item='sea'))
#     # The sea lives in the sea

# # other ways to display formating fields

# text = 'The {} saw the {}'
# print(text.format(animal,item))
    # The turtle saw the sea

name = 'Toad'
print('Mr. {}, likes to croak'.format(name))
    # Mr. Toad, likes to croak

# add some padding right side of format field
print('Mr. {:10}, likes to croak'.format(name))
    # Mr. Toad      , likes to croak

# left align, center align, right align

# to left align use the less than sign -- no visible changes because it is already the default
print('Mr. {:<10}, likes to croak'.format(name))
    # Mr. Toad      , likes to croak

# to right align precede your number is a greater than sign  -- value will be right aligned
print('Mr. {:>10}, likes to croak'.format(name))
    # Mr.       Toad, likes to croak
    
# to center align use the carrot ^
print('Mr. {:^10}, likes to croak'.format(name))
    # Mr.    Toad   , likes to croak

# what if we need to add a positional argument or keyword argument to our format field if there's already some text within the braces
print('Mr. {0:10}, likes to croak'.format(name))
    # Mr. Toad      , likes to croak
print('Mr. {1:10}, likes to croak'.format(name, 'Rogers'))
    # Mr. Rogers    , likes to croak

# format numbers

number = 3.14159 # want to display 2 decimal points
print('The number pi is {:.2f}'.format(number))
    # The number pi is 3.14
# display 3 decimal points
print('The number pi is {:.3f}'.format(number))
    # The number pi is 3.142

number = 1000 # want to add a comma to the thousands place
print('The number pi is {:,}'.format(number))
    # The number pi is 1,000
# displays binary representation of your number
print('The number pi is {:b}'.format(number))
    # The number pi is 1111101000
# displays number as octal number
print('The number pi is {:o}'.format(number))
    # The number pi is 1750
# displays number in hexadecimal
print('The number pi is {:x}'.format(number))
    # The number pi is 3e8
print('The number pi is {:X}'.format(number))
    # The number pi is 3E8
# display number in scientific notation
print('The number pi is {:e}'.format(number))
    # The number pi is 1.000000e+03
print('The number pi is {:E}'.format(number))
    # The number pi is 1.000000E+03

