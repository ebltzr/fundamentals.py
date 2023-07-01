rows = int(input('How many rows '))
columns = int(input('How many columns '))
symbol = input('Enter a symbol to use ')

# outer for loop iterate as many times as we have rows 
for i in range(rows):
    # inner for loop iterate as many times as we have columns
    for j in range(columns):
        # currently within inner for loop
        # end="" this will prevent cursor from going down to the next line
        print(symbol, end="")
    # print a new line within the outer for loop
    print()
    # How many rows 3
    # How many columns 9
    # Enter a symbol to use $
    # $$$$$$$$$
    # $$$$$$$$$
    # $$$$$$$$$