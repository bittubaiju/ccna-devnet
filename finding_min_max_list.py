x=[]
n = int(input('total num of elements: '))
for i in range(n):
    x.append(int(input('enter the element: ')))
print('list is: ',x)
big = x[0]
small = x[0]
for i in range(n):
    if x[i]>big: #
        big = x[i] #will put the biggest list element to this big.
    if x[i]<small:
        small = x[i] #will put the smalles list element to this value.
print('biggest value is %d and smallest values is %d'%(big,small))