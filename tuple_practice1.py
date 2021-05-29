#program to accept the number in tuple and print the sum of the values.
'''x = []
sum = 0

n = int(input('total num of elements: '))
for i in range(n):
    x.append(int(input('enter the element: ')))
print('list is: ',x)
tup = tuple(x)
print('tup is :',tup)
for i in tup:
    sum = sum+i
print('sum of tup is: ',sum)'''
# OR another of taking input for tuple is through EVAL function
'''num = eval(input('enter element in (): '))
print(num)
sum = 0
n = len(num)
for i in range(n):
    sum = sum + num[i]
print(sum)
# when group of elements are entered in , they are by default considered as tuple.'''
# tuple packing and unpacking(Ex:Swapping a,b=b,a)
a= 'bittu',24,43.5,'Male' #packing the values
(name,age,marks,gender)=a #unpacking the values.
print(name,age)