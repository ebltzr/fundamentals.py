# \n is making a new line
text = 'Howdy howdy\nReach for the starts\nBuzzbuzzbuzz'

# without a print statement this will be written and overwrite previous text in reading-files.txt -- run code see text displayed not in terminal but in txt file
with open('reading-files.txt', 'w') as file:
    file.write(text)
    # Howdy howdy
    # Reach for the starts
    # Buzzbuzzbuzz

# even though code above still exists (or if it didn't) this new text overwrites it
# text = 'Text overwrite'

# with open('reading-files.txt', 'w') as file:
#     file.write(text)
        # Text overwrite

# append a file -- use mode a
# because there is no \n at the end or beginning of text new appended text has no space or new line
text = 'Text overwrite'

with open('reading-files.txt', 'a') as file:
    file.write(text)
        # Howdy howdy
    # Reach for the starts
    # BuzzbuzzbuzzText overwrite

# new line append text -- added \n to beginning of text
text = '\nText overwrite'

with open('reading-files.txt', 'a') as file:
    file.write(text)
        # Howdy howdy
    # Reach for the starts
    # Buzzbuzzbuzz
    # Text overwrite