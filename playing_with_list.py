#program to count the number of times a value occured in a list.
'''x=[1,2,3,4,2,3,4,5,6,3,4,5]
count = 0
n = int(input('enter the value to be searched: '))
for i in x:
    if n==i:
        count+=1

print('The value %d occured %d times'%(n,count))'''

# finding common elements in list
sh1 = ['Bittu','Achu','Amma','Acha']
sh2 = ['Bittu','Neha','Dhaval','Shaurya','Achu']

s1 = set(sh1)
s2 = set(sh2)
print(s1&s2) #intersection of set1 and set2


