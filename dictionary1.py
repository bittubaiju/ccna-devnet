""" dictionaries are key value pair.
 Ex: d = {key1:value1,key2:value2,key3:value3}
 each key:value pair is one element in dict
 dict is immutable"""
dict = {'name':'Bittu','age':24,'gender':'Male'}
print('Name is: ',dict['name']) #accessing the value is through key.
print('Age is: ',dict['age']) #key is acting as index in dictionary
print('Gender is: ',dict['gender'])
dict['age'] = 30 #to update dict values. key's are immutable so we cannot use list or dict for keys.
print(dict['age'])
print(len(dict)) # each key:value pair is 1 element in dict.
dict['salary']=3000.00 # inserting a new value to dict
print(dict)
del dict['age'] # deleting dict value
print(dict)
print('age' in dict) # will return boolean, will check for this key in dict
print('age'not in dict) # age is not in the dict
#repeating same key in dict but this time with diff value
dict = {'name':'Bittu','age':24,'gender':'Male','age':30}
print(dict) # if repeating key then will update with the latest, keys are unique in dict