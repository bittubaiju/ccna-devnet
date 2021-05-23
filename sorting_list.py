x=[]
n = int(input('total num of elements: '))
for i in range(n):
    x.append(int(input('enter the element: ')))
print('list is: ',x)
already_sorted = True
for i in range(n-1):
    for j in range(n-1-i):
        if x[j]>x[j+1]:
            x[j],x[j+1]=x[j+1],x[j]
            already_sorted = False
    if already_sorted:
        break

print('sorted list is ',x)
