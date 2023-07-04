# this variable is known to have a local scope because it is declared inside of a function
def display_name():
    name = 'Only In' # local scope ( available only inside this function)
    print(name)
    
# print(name)
    # NameError: name 'name' is not defined

# global variable that is declared outside of any function but within your module that you are working with
name = 'In n Out' # global scope (available inside & outside functions)
def display_name():
    name = 'Only In'
    print(name)
    
print(name)
    # In n Out

# use local version variable before the global version of the variable
name = 'Global' 
def display_name():
    name = 'Local'
    print(name)

display_name() 
    # Local
print(name)
    # Global
    

