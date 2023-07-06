# Python Tutorial

  - install python
  - install integrated developement enviornment ie PyCharm, VSCode
    - this is a software that helps us write other software

## Create New Project

  - Go onto IDE and create new project
      - Name project "Hello World"
  - Terminal window
  - print a message
      - print('Hello World') -- run -- see terminal window of printed string
      - print("Hello World") -- run -- see terminal window of printed string

## Variables 
  - a variable = container for a value. behaves as the value that it contains
  - 4 basic datatypes
      - strings (str): which store a series of characters 
      - integers (int): which store a whole number 
      - floating point number (float): a numeric vlaue with a decimal
      - booleans (bool): which only store True or False, very useful with if statements
        - ie x = 2 + 5 x = 7
  - variable string "Hello"
  - variable integer 21
  - variable float 2.5 
  - variable boolean false/true
  - You can combine variables together as long as they are of the same datatype

- the reason you may want to use booleans instead of str even though you can still store a str representation of the word false or true is that, these are very useful when we get to if statements. we can check to see if some statement is true/false

## Multiple Assignment

  - multiple assignment: allows us to assign multiple variables at the same time at the same time using one line of code

## String methods

  - length method (len):
  - find method (.find("x"))
  - capitalize (.capitalize())
  - upper (.upper())
  - Alphabetical letters (.isalpha())

## Type Casting

  - type casting = convert the datatype of a value to another datatype

## User-Input

## Math Functions

  - round : nearest whole int
  - ceiling (math.ceil()) : nearest whole int rouding up
  - floor (math.floor()) : nearest whole int rouding down 
  - absolute value function (abs): gives absolute value of a number, how far away a number is from zero -- even when given a negative number it will return positive
  - power function (pow): will raise a base number to a power
    - print(pow(base, exponent))
  - Square root (sqrt): find the sqaure root of variable -- does not work on negative 

## Slicing

  - slicing: create a substring by extracting elements from another string indexing[] or slice()
    - [start:stop:step]


## If Statements
-  a block of code that will execute if it's condition is true

## logical operators

- and, or, not -- logical operators focused on and , or 
- used to check if two or more conditional statements are true

## while Loops
- a statement that will execute it's block of code as long as it's condition remains true
- can cause an infinite loop

## for Loops
- a statement that will execute it's block of code a limited amount of times
  - while loop = unlimited
  - for loop = limited
  
## Nested loops
- for loop or while loop -- concept of having one loop inside of another
- the 'inner loop' will finish all of it's iterations before we finish one iteration of the 'outer loop'

## Loop Control Statements
- change a loops execution from its normal sequence
- break = used to to terminate the loop entirely
- continue = skips to the next iteration of the loop
- pass = does nothing, acts as a placeholder

## Lists
- used to store multiple items in a single variable
    - print list
    - print list with given index
    - change index value
    - .append: add value to end of list
    - .remove: removes value from list
    - .pop: removes last value from list
    - .insert: add value to given index
    - .sort: sort list alphabetically
    - .clear: clears all the elements of a list, so this will not print anything

### *2D Lists*
  - list of lists
  - multidimensional list
  - if you need to access one of the elements within your 2D list, you need two sets of brackets [][]

### *Tuples*
  - collections very similar to list but are ordered and unchangeable, used to group together related data
    - like list but instead of square bracketss [] you use paraentheses ()

### *Set*
  - collection different from list because they are unordered, unindexed. No duplicate values
  - - .add: add value to end of list
    - .remove: removes value from list
    - .clear: clears all the elements of a list, so this will not print anything
    - .update: add one set to another
    - .join: two sets together and create a new set entirely
    - .difference: compare similarities/differences in sets
    - .intersection: check if sets have anything in common

## Dictionary
  - changeable (ie mutable), unordered collection of unique key:value pairs 
  - they are FAST because they use hashing, that allow us to access a value quickly
  - creating a dict is very similar to creating a set except we ar going to store unique key, value pairs
    - in order to access one of these values value instead of using a numbered index we use the associated key
      - .get method; safer way of checking if there is a key within your dict
      - .keys method; this will print only the keys and not the values
      - .values method; this will print only the values and not the keys
      - .items method; print entire dict
          - another way to print entire dict is for loop
      - .update: to add a new key:value pair
          - to update an existing key:value pair
      - .pop: to remove a key:value pair
      - .clear: to clear entire dict

## Index Operator 
  - represented by a set of square brackets []
  - gives access to a sequence's element include but not limited to
      - str (example focused)
      - list
      - tuples
  - create substring [start:end] from the first part of name, this substring start at index[0] and end at index[4] ie rico index 0,1,2,3
  - negative indexing ie -1 is the last letter of string
  
## functions
- a block of code which is executed only when it is called
  - function can perform some specific task whenever it is called, instead of writing code repeatedly you only need to write that block of code once and call it when you want to use it
- in functions we can pass arguments to function and our function can do something with those arguments

## return statement
- functions send python values/objects back to the caller
  - these values/objects are known as the functions return value
- function can pass some value/object back to the called
  - print to the console window or store within variable or other location

## keyword arguments 
- arguments preceded by an identifier when we pass them to function
- The order of the arguments *DOESN'T* matter unlike positional arguments Python knows the names of the arguments that our function receives
  - positional arguments:
def hello(first,middle,last):
  print('Hello '+first+' '+middle+' '+last)

hello('last','mid','first')
  *Hello last mid first*

- precede each argument with a unique identifier (id) -- id is the name of the parameter (ie first) we want to associate each argument with
  - keyword arguments:
def hello(first,middle,last):
  print('Hello '+first+' '+middle+' '+last)

hello(last='last',first='first',mid='mid')
  *Hello first mid last*

## Nested function calls
- function calls inside other function calls
  -  this is possible because certain functions will return a value and we can immediately use that value as an argument for the next function
- innermost function calls are resolved first
- return value is used as an argument for the outer function

## Scope (variable)
- region that a variable is recognized
  - a variable is only available from inside the region it is created
- global and locally scoped versions of a variable can be created 
- it is possible to have a local and global verison of the same named variable
  - you will first use local version available and then global
- **PYTHON RULE:**
  - L = Local (use local variables first)
  - E = Enclosing
  - G = Global
  - B = Built-in

## *args Parameter
- parameter that will pack all arguments into a tuple, useful so that a function can accept a varying amount of arguments
- *args can be named anything but has to have the asterisk -- this is form of packing, we are passing all of these arguments and packing them into a tuple
  - one way to change from tuple to list is by casting
  - args stands for arguments

  ### **kwargs Parameter
- parameter that will pack all arguments into a dictionary, useful so that a function can accept a varying amount of keyword arguments 
- identical to *args EXCEPT with *args, *args will accept a varying amount of postional arguments and pack them into a tuple. *kwargs accepts a varying amount of keyword arguments and pack them into a dictionary
- **kwargs can be named anything like *args but important thing is the double asterisks 
- kwargs stands for keyword arguments

## format method
- optional method that gives users more control when displaying output
- available to strings (only)
- use format fields with curly braces {} : they function as a placeholder for a value or variable
    - they work in order they are give, first format field with first value, second format field with second value etc
- also has varying number formats
  - {.2f} -- display 2 decimal points
  - {.3f} -- display 3 decimal points
  - {:,} -- want to add a comma to the thousands place
  - {:b} -- displays binary representation of your number
  - {:o} -- displays number as octal number
  - {:x} -- displays number in lowercase hexadecimal
      - {:X} -- displays number in uppercase hexadecimal
  - {:e} -- display number in lowercase scientific notation
      - {:E} -- display number in uppercase scientific notation

## random module
- import random <-- must import
- generate some random numbers and other useful ranom methods
  - random.randint : this will give us a random number between specified values
  - random.random : this will give us a random number between 0 and 1
  - random.choice : this will display random choice from list
  - random.shuffle : this will output list with shuffled values

## exception handling
- events dected during execution that interrupt the flow of a program
- it is not considered good practice to have a single except block that will handle all exceptions
  - it's much better to first handle specific exceptions when they occur
    - except Exception : print whatever you want
    - except ZeroDivisionError: ZeroDivisionError: division by zero
    - except ValueError: ValueError: invalid literal for int() 
    - can use an else statement after exception without an if conditional
    - finally : always at the end, whether or not we encounter an exception always is executed
    - good opportunity if you open files, to close them within the finally ( no files in this example)

# Doing things with files section

## File Dectection
- import os module
- checking to see if a file exists some place in our computer

## Reading a file 