a = [1,2,3,4,'bittu',10.4]
print(a)
b = [] #initilizing a string or b = list()
print(a[1]) #this one working here but not working in strings had to use -2 to fetch last value
a.append('achu') #takes only 1 arguement
print(a)
print(a.index(3))
print(a.pop(4)) #removes the given value from the list
print(a.remove(1)) #removes the given value and returns none. arguement taken value not index
print(type(a))
#TUPLES
tpls = ('bittu','achu','amma') #tuples are immutable so if we have some data which we dont tochangethentupleistheoption
print(tpls[0])
print(type(tpls))
#DICTIONARY
''' list is oredered set which can be accessed with index, but what if we want to access some data which is tied to
some key value. so in this case comes dictionary
dictionary: consist of key value pair. where value can be accessed with his key.'''
info = {'name':'bittu','age':24,'gender':'male'}
print(info['name']) #with the help of key we print the value
#SETS
num = {1,2,3,4,5}
odds = {1,3,5,7}
print(num|odds) # joints 2 sets and print non repetitive values.
print(num&odds) #intersection of 2 sets.