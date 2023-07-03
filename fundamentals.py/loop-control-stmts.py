# break

# while True:
#     name = input('Enter your name ')
#     # this loop will repeat until it receives an input, code terminated after 'Lame' input
#     if name != "":
#             break
    # Enter your name 
    # Enter your name 
    # Enter your name 
    # Enter your name 
    # Enter your name Lame



# continue control statement skips to the next iteration of the loop   

phone_number = "123-456-7890"
# for each character [i] in our string phone_number, check to see..
for i in phone_number:
    # this if conditional removes - from phone_number string
    if i == "-":

        continue
    #using the print statement, prints each [i] in a new line
    # print(i)
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9
    # 0
    # instead add ,end='' this will print phone_number without any dashes or new lines
    print(i, end="")
    
# print("matt")


# pass -- pass does nothing, it acts as a placeholder

for i in range(1,11):
    
    if  i == 4:
    # this skips 4 because we used the pass control statement
        pass
    else: 
        print(i)
    # 1
    # 2
    # 3
    # 5
    # 6
    # 7
    # 8
    # 9
    # 10
    