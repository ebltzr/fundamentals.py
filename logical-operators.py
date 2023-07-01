temp = int(input('What is the temp outside? '))

# both of these statements have to be True
if temp >= 0 and temp <= 30:
    print('Go outside')
    print('The temp is good today')
    # What is the temp outside? 30
    #     Go outside
    #     The temp is good today
    
    # What is the temp outside? -20
        # no output because statement is False
        
# as long as one statement is True the whole statement is True
elif temp < 0 or temp > 30:
    print('The temp is bad today')
    print('Stay inside')
    # What is the temp outside? -20
    #     The temp is bad today
    #     Stay inside
    

# the not operator    
if not temp >= 0 and temp <= 30:
    print('The temp is bad today')
    print('Stay inside')
    # What is the temp outside? 15
    #     Go outside
    #     The temp is good today

elif not temp < 0 or temp > 30:
    print('Go outside')
    print('The temp is good today')