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
def hello(name):
    print('Hello ' + name)
hello('Sup')
    # Hello Sup