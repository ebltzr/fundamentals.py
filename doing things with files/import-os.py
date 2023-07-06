import os

path = '/Users/ed/Desktop/Screenshot 2023-06-08 at 5.44.42 PM.png'

if os.path.exists(path):
    print('Location Found')
    if os.path.isfile(path):
        print('File Found')
    elif os.path.isdir(path):
        print('I am a directory')
else:
    print('Location not Found')
    # Location Found
    # File Found
        
path = '/Users/ed/Documents/Developer'

if os.path.exists(path):
    print('Location Found')
    if os.path.isfile(path):
        print('File Found')
    elif os.path.isdir(path):
        print('I am a directory')
else:
    print('Location not Found')
        # Location Found
        # I am a directory