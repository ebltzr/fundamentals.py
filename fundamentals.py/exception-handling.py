try:
    numerator = int(input('Enter a number to divide: '))
    denominator = int(input('Enter a number to divide by: '))
    result = numerator/denominator
    print(result)
        # Enter number to divide: 5
        # Enter number to divide by: 0
            # ZeroDivisionError: division by zero
except ZeroDivisionError as e:
    print(e)
    # ZeroDivisionError: division by zero
    print('You can\'t divide by zero')
except ValueError as e:
    print(e)
    # ValueError: invalid literal for int() 
    print('Enter only numbers please')
except Exception as e:
    print(e)
    print('something went wrong')
        # something went one
# can add else statement
else:
    # when running code does not encounter an exception
    print(result)
        # Enter number..: 5
        # Enter number..: 2
            # 2.5
finally:
    # whether or not encountering an exception
    print('This always executes')