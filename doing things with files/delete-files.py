import os
import shutil

# deleting copy.txt created in copy-files
path = 'reading-files.txt'

# os.remove(path)
    # this code deleted the file

    # after deleting file, tried to run code again received error below
# FileNotFoundError: [Errno 2] No such file or directory: 'copy.txt'

# try except for fileNotFound, permissionError, osError, remove, rmdir, rmtree

# path = 'copy.txt'
# path = 'empty_folder'
path = 'folder'

try:
    os.remove(path) # delete a file
    
    # to delete an empty folder or directory -- rmdir is remove directory -- this function will not delete a folder/directory that is not empty
    os.rmdir(path) # delete an empty directory
    
    # to remove a folder/directory -- **!CAUTION!** -- this function will delete a folder/directory and all files contained within
    shutil.rmtree(path) # delete a directory containing files

except FileNotFoundError:
    print('File not Found')
# Permission -- appears when trying to delete an empty folder 
except PermissionError:
    print('You do not have permission to delete that')
# OS -- appears when trying to delete folder/directory that is NOT empty
except OSError:
    print('You cannot delete that (folder/dir) using rmdir function')
# output when no errors are displayed and something is deleted
else:
    print(path+' was deleted')
        # empty_folder was deleted // rmdir
        # folder was deleted // rmtree

