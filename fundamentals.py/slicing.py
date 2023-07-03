# [start:stop:step]

name = "Tater Tot"

first_name = name[0]

print(first_name) # T -- [start]

# if we would like to slice an entire portion of our string not just one letter we need a [stop] index as well
first_name = name[0:4] # Tate -- even though the index for the first name is 0-4 the output is Tate because the first index [start] is inclusive and the second index [stop] is exclusive 
print(first_name) 

first_name = name[0:5]
print(first_name) # Tater

#shortcut
first_name = name[:5] # Tater -- python assumes that this is index[0] at the beginning of your str
print(first_name)

last_name = name[5:9] # Tot -- this starts at index[5] and ends at the last index 
print(last_name)

#shortcut
last_name = name[5:] # Tot -- python assumes to start at index[5] and output everything after as well
print(last_name)

#[step]
# step_name = name[0:9:1]
# print(step_name) # Tater Tot
# 
# # step_name = name[0:9:2] # TtrTt -- displays every second character including the first character
# print(step_name)
# 
# step_name = name[0:9:3]
# # print(step_name) # TeT -- displays every third character including the first character
# 
#shortcut
step_name = name[::1], name[::2], name[::3] # ('Tater Tot', 'TtrTt', 'TeT')
print(step_name)

step_name = name[::2]
print(step_name) # TtrTt -- python will assume that index[start] is index[0] and index[stop] is the end of your str.  So just having two colons and then index[step]