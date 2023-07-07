# Doing things with files section
    - if you have single backslashe \ then you will have to change them to double \\ backslashes because that is the escape sequence to print a backslash within a string
  - deleted both example files created

## File Dectection
- import os module
- checking to see if a file exists some place in our computer

## Reading a file 
- with open -- opens and closes file automatically
    - when using with open use 'r' for read
  
## Writing in a File
- when using with open use 'w' for write
- append a file by using 'a' for append

## Copy files
- import shutil module
- copyfile() : copies contents of a file
- copy() : copyfile() + permission mode + destination can be a directory
- copy2() : copy() + copies metadata (files creation and modification times)

## Moving files
- import os module
- create variables, to file/directory/folder wanting to move/find/see if a file is there
    - include the path to move file or find file
    - .exists : to figure out if file/path exist
    - .replace : to move file/path
    - 

## Delete files
- import os
- .remove : to delete path/file
- .rmdir : remove (empty) folder and/or directory
- .rmtree : delete a folder/directory containing files

## Modules
- is a file containing python code, it may contain functions classes etc
- it is used with modular programming : concept of separating a program into useful different parts 
- import (name of module) : to import module
- import (name of module) as (alias/nickname) : don't have to write full module name
- from (name of module) import (classes, functions) : don't have to write module name to call, only name of class/function 
- * : to import all -- only use for small projects, can run into naming conflict
- help('modules') : to see pythons prewritten modules
- https://docs.python.org/3/py-modindex.html : list of modules as well
