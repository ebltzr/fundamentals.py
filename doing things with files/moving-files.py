import os

source = 'reading-files.txt'
destination = '//Users//ed//Desktop//reading-files.txt'

# in case file cannot be found
try:
    if os.path.exists(destination):
        print('there is already a file there')
    else:
        os.replace(source, destination)
        print(source+' was moved')
except FileNotFoundError:
    print(source+' was not found')

# when leaving normal and using single slashes file is not found
destination = '/Users/ed/Desktop/reading-files.txt'
        # reading-files.txt was not found

# when using doubles slashes file is moved
destination = '//Users//ed//Desktop//reading-files.txt'
        # reading-files.txt was moved

# moving a folder or directory example
source = 'folder'
destination = '//Users//ed//Desktop//folder'
