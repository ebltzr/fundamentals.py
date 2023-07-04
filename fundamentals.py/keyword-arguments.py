# positional arguments: order of the arguments matters
def hello(first,middle,last):
  print('Hello '+first+' '+middle+' '+last)

hello('first','mid','last')
    # Hello first mid last
hello('last','first','mid')
    # Hello last first mid

# keyword arguments: order of arguments doesn't matter -- but we need to precede each argument with a unique identifier (id) -- id is the name of the parameter (ie first) we want to associate each argument with

def hello(first,middle,last):
    print('Hello '+first+' '+middle+' '+last)

hello(last='last',first='first',middle='mid')
    # Hello first mid last