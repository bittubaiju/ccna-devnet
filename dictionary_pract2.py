# converting a given string into dictionary.
'''lst = []
str1 = 'bittu=24,achu=20,amma=44,acha=50'
for i in str1.split(','):
    y = i.split('=')
    lst.append(y) # is a list of list were each inner list is a name and age

dict1 = dict(lst)
print(dict1) # but here age is string but we need it in int.

for k,v in dict1.items():
    dict1[k]= int(v)
for k in dict1: # or we could use items() func also but then we need 2 variable
    print('{} age is {}'.format(k,dict1[k]))'''
#passing function to a dictionary
def fuc(d):
    for k,v in d.items():
        print('{} ---> {}'.format(k,v))

d={'A':'Apple','B':'Ball','C':'Cat','D':'Dog'}
fuc(d)
