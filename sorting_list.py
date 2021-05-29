x=[]
n = int(input('total num of elements: '))
for i in range(n):
    x.append(int(input('enter the element: ')))
print('list is: ',x)
already_sorted = True
for i in range(n-1): #beacuse range starts from 0
    for j in range(n-1-i): #so that j won't go upto last element as it is already sorted
        if x[j]>x[j+1]:
            x[j],x[j+1]=x[j+1],x[j] #swaping because it is possible in python without temp variable
            already_sorted = False
    if already_sorted: #in case the list is already sorted.
        break

print('sorted list is ',x)
