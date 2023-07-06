# this file is in the main project folder -- if it is anywhere else it will need the file path instead

# with open -- automatically opens and closes files, after they've been opened
with open('reading-files.txt') as file:
    print(file.read())
#     # Holy Cow
#     # Bazinga
#     # Tralalala
# # this is verifying if file is open or closed
print(file.closed)
    # True

with open('reading-files.tx') as file:
    print(file.read())
        # FileNotFoundError: [Errno 2] No such file or directory: 'reading-files.tx'

# create try/except not FileNotFoundError
try:
    with open('reading-files.tx') as file:
        print(file.read())
except FileNotFoundError:
    print('Exception: File not Found')
        # Exception: File not Found
