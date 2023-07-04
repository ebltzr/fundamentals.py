# add a set of [] after a string, list or tuple and then list an integer or a range of the elem that you are trying to access

name = 'rico Suave'

# with computers first elem is 0
# check if first letter (index[0]) is lower case
if (name[0].islower()):
    name = name.capitalize()
print(name)
    # Rico suave
    
# create substring from the first part of name
# this substring start at index[0] and end at index[4]
first_name = name[0:4].upper()
# if your index[0] for your range[4] begins with 0 you can delete 0 --> [:4]
print(first_name)
    # RICO
    
# now to display that last name start at index first letter of last name in this case index[5] you can leave the end blank because you want to display range til the final letter
last_name = name[5:].lower()
print(last_name)
    # suave
    
# negative indexing
last_character = name[-1].upper()
print(last_character)
    # E
# second to last elem in sequence
last_character = name[-2]
print(last_character)
    # v