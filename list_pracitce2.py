lst1 = [10,20,30,40,50,60]
'''i = 0
print(len(lst1))
while i < len(lst1): # will go up to n-1 value which in this case is 6-1=5
    print(lst1[i])
    i += 1
print('with for loop')
for j in lst1:
    print(j)'''
lst1[1]=10 #updating the list variable
lst1[1]=100,200,300,400,500,600 # can update the list with multiple values also which will become a tuple.
print(lst1)
print(lst1[2])
i=5
while i>=0: #reversing a list.

    print(lst1[i])
    i-=1

