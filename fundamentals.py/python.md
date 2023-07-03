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

## 2D Lists
  - list of lists
  - multidimensional list
  - if you need to access one of the elements within your 2D list, you need two sets of brackets [][]

## Tuples
  - collections which is ordered and unchangeable used to group together relate data