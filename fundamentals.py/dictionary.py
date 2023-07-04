capitals = {
            'usa': 'washington dc',
            'india':'new dehli',
            'china': 'beijing',
            'russia': 'moscow'
            }
# in order to access one of these values value instead of using a numbered index we use the associated key ie 'usa' / 'india' / 'china' / 'russia'
print(capitals['russia'])
    # moscow
    
# this key does not exist -- will encounter an error
# print(capitals['germany'])
    # KeyError: 'germany'

# get method of dict; safer way of checking if there is a key within your dict
print(capitals.get('germany'))
    # None
    
# keys method -- this will print only the keys and not the values
print(capitals.keys())
    # dict_keys(['usa', 'india', 'china', 'russia'])

# values method -- this will print only the values and not the keys
print(capitals.values())
    # dict_values(['washington dc', 'new dehli', 'beijing', 'moscow'])
    
# items method -- print entire dict
print(capitals.items())
    # dict_items([('usa', 'washington dc'), ('india', 'new dehli'), ('china', 'beijing'), ('russia', 'moscow')])

# another way to display entire dict
for key, value in capitals.items():
    print(key, value)
    # usa washington dc
    # india new dehli
    # china beijing
    # russia moscow

# dict is mutable, which  means we can change them or alter them after the program is already running

# update method of dict -- to add a new key:value pair
capitals.update({'germany':'berlin'})
for key, value in capitals.items():
    print(key, value)
    # usa washington dc
    # india new dehli
    # china beijing
    # russia moscow
    # germany berlin
    
# update method of dict -- to update an existing key:value pair
capitals.update({'usa':'las vegas'})
    # update -- usa:washington dc --> usa:las vegas
for key, value in capitals.items():
    print(key, value)
    # usa las vegas
    # india new dehli
    # china beijing
    # russia moscow
    # germany berlin

# pop method -- to remove a key:value pair
capitals.pop('china')
    # this will remove china:beijing
for key, value in capitals.items():
    print(key, value)
    # usa las vegas
    # india new dehli
    # russia moscow
    # germany berlin
    
# clear method -- to clear entire dict
capitals.pop('china')
for key, value in capitals.items():
    print(key, value)
    # ** nothing **