# length method
name = "Modelo"

print(len(name)) # 6

name_2 = "Modelo Cat"

print(len(name_2)) # 10


#find method -- how to find a character within a str
print(name.find("M")) # 0 -- index 0
print(name.find("o")) # 1 .. what about second 'o' ?
print(name.find("o")) # only finds first character


# capitalize 
name = "modelo cat"

print(name.capitalize()) # Modelo cat
print(name.upper()) # MODELO CAT
print(name.isalpha()) # False -- because there is a space

name_2 = "MoDelO cATo"
print(name_2.lower()) # modelo cat
print(name_2.isdigit()) # False
print(name_2.count("o")) # 2 -- only counts letter provided specifically upper/lower
print(name_2.count("O")) # 1 -- only one uppercase 'O'


name_3 = "2345"
print(name_3.isdigit()) # True

name_4 = "Modelo" 
print(name_4.isalpha()) # True -- check to see if your str is only alphabetical letters
print(name_4.count("o")) # 2 -- count how many characters are in our str 
# print(name_4.count()) # TypeError: count() takes at least 1 argument (0 given)
print(name_4.replace("o", "a")) # Madela -- two arguments the character we like to replace and the character we would like to replace our character with ie change all 'o' to 'a'
print(name_4*3) # ModeloModeloModelo
