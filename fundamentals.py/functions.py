def hello():
    # code under function becomes indented
    print('hello')
# in order to call this function -- function always ends with set of ()
hello()
    # hello

# hello function will be called three separate times
hello()
hello()
hello()
    # hello
    # hello
    # hello
    
#functions are not limited to just one line -- prints function 3 times
def hello():
    print('Hello')
    print('Have a nice day')
    
hello()
hello()
hello()
    # Hello
    # Have a nice day
    # Hello
    # Have a nice day
    # Hello
    # Have a nice day
    
# we can send our function some information
def hello():
    # currently name is an unresolved reference
    print('Hello ' + name)

# send function information -- value, variable, collection -- within the () add the data you would like to send your function
    # arguments: information that you are sending to a function and when you define that function you need a matching set of parameters
        # our function receives one argument a string value 'Sup' ; we need a matching number of parameters
# hello('Sup')
    # TypeError: hello() takes 0 positional arguments but 1 was given
    
# list the parameters within the paraentheses of that function
    # we have a matching set of arguments and parameters
        # when we call the hello function 
            #  we are sending one argument over 
                # when hello function receives this argument, we are going to give it a temporary nickname of name -- parameter -- and we can use this function for whatever we want in our function

# pass function a string ie argument
def hello(name):
    print('Hello ' + name)
hello('Sup')
    # Hello Sup
    
# pass function a variable
def hello(name):
    print('Hello ' + name)
name = 'Lalo'
    
hello(name)
    # Hello Lalo

# variable name does not have to be the same as parameter
def hello(name):
    print('Hello ' + name)
my_name = 'jr'
    
hello(my_name)
    # Hello jr
    
# with arguments you can send more than one value over -- send two values over -- this won't work because there isn't a matching set of arugments and parameters
def hello(name):
    print('Hello ' + name)
    
hello('First', 'Last')
    # TypeError: hello() takes 1 positional argument but 2 were given
    
def hello(first, last):
    print('Hello ' + first + last)
    
hello('First', 'Last')
#     # Hello FirstLast
    
def hello(name):
    print('Hello ' + name)

    
hello('First', 'Last', 30)
    # TypeError: hello() takes 1 positional argument but 3 were given

    
def hello(first, last, age):
    print('Hello ' + first +" "+ last)
    print('You are ' +str(age)+ ' years')
    
hello('First', 'Last', 30)
    # Hello First Last
    # You are 30 years