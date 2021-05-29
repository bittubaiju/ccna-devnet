# using loops to fetch dictionary values.
'''dict = {'r':'red', 'b':'black', 'g':'green', 'w':'white'}
for k in dict:
    print(k,end=':') # will only print keys
    print(dict[k]) # will fetch the values
for k,v in dict.items(): # to fetch the whole dict using for loop
    print('key = {}, value = {}'.format(k,v))'''
# program to find the occurence if each word from a string
'''dict = dict()
str1 = input('enter the string: ')
for x in (str1):
    dict[x] =dict.get(x,0)+1#will store word as key and occurence as value.+1 coz initially there is no occur ofeachword
print('occurence of each word from string ')
print(dict)'''

lst1 = ['USA','INDIA','JAPAN','NORWAY','MEXICO']
lst2= ['washington','new delhi','tokyo','oslo','mexico city']
''' now we want to convert both list into dictioanry,
country name will become key and capital will become value
we will accomplish this task using zip function
zip: will convert the sequence into zip objects'''
z = zip(lst1,lst2) #we can pass any number of objects in our case it is 2 i.e: lst1,lst2
print(z) #zip is a class.
dict1 = dict(z)
print(dict1)
for k in dict1:
    print('{} capitol is {}'.format(k,dict1[k]))