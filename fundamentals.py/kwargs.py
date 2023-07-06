
def hello(first, last):
    print('Hello '+ first+' '+last)
    
hello(first='first',last='last')
    # Hello first last

# what if someone has a middle name
def hello(first, last):
    print('Hello '+ first+' '+last)
    
hello(first='first',middle='mid',last='last')
    # TypeError: hello() got an unexpected keyword argument 'middle'

# use **kwargs parameter -- replace parameters
def hello(**kwargs):
    # in order to access a value within a dict, type the name of the dict (ie kwargs) [] and list your key inside [] (ie kwargs['first'])
    print('Hello '+ kwargs['first']+' '+kwargs['last'])
    
hello(first='first',middle='mid',last='last')
    # Hello first last

# display full name --  using for loop -- iterate once through each key:value pair within this dict
def hello(**kwargs):
    print('Hello '+ kwargs['first']+' '+kwargs['last'])
    print('Hello')
    for key,value in kwargs.items():
        print(value)
    
hello(first='first',middle='mid',last='last')
    # Hello
    # first
    # mid
    # last
# OR no new lines -- ,end=' '
def hello(**kwargs):
    print('Hello '+ kwargs['first']+' '+kwargs['last'])
    print('Hello', end=' ')
    for key,value in kwargs.items():
        print(value, end=' ')
    
hello(first='first',middle='mid',last='last')
    # Hello first mid last
# AND add more varying keywords
def hello(**kwargs):
    print('Hello '+ kwargs['first']+' '+kwargs['last'])
    print('Hello', end=' ')
    for key,value in kwargs.items():
        print(value, end=' ')
    
hello(title='Mx',first='first',middle='mid',last='last')
    # Hello Mx first mid last

# change kwargs to anything, important part is asterisks -- change name of dict (ie names)
def hello(**names):
    print('Hello '+ names['first']+' '+names['last'])
    print('Hello', end=' ')
    for key,value in names.items():
        print(value, end=' ')
    
hello(title='Mx',first='first',middle='mid',last='last')
    # Hello Mx first mid last