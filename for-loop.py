
for i in range(7):
    print(i)
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6

for i in range(7):
    print(i+1)
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    
# the first number (50) is inclusive and the second number (100) is exclusive
for i in range(50, 55):
    print(i)
    # 50
    # 51
    # 52
    # 53
    # 54

# this iterates 5x be aware of iteration count
for i in range(50, 55+1):
    print(i)
        # 50
        # 51
        # 52
        # 53
        # 54
        # 55
        
# this will count up by 2 starting at 50 up to the final 2 count
for i in range(50, 55+1, 2):
    print(i)
    # 50
    # 52
    # 54
    
# we can iterate through anything that is considered iterable this could include a string, letters of a string or any sort of collection
for i in "Jerry Springer":
    print(i)
    # J
    # e
    # r
    # r
    # y

    # S
    # p
    # r
    # i
    # n
    # g
    # e
    # r
    
# import time module -- at the top
import time

# starting point is 10, ending point is 0, step is -1 (count up or down ) 
for seconds in range(10, 0, -1):
    # print i or in this case seconds
    print(seconds)
    # have thread sleep for a matter of seconds -- thread in this program is sleeping for one second after each iteration of this for loop, then once we reach zero it displays Happy New Year
    time.sleep(1)
print("Happy New Year")
    # 10
    # 9
    # 8
    # 7
    # 6
    # 5
    # 4
    # 3
    # 2
    # 1
    # Happy New Year