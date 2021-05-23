# Tuples are immutable means once values are assigned we cannot modify the values.

x = (10,) #if we dont give , then it will consider x as int and not tuple
y = [10]
print(x)
print(y)
print(type(x),type(y))
a = 10,20,30 #if we dont bracket also it will consider as tuple but not in the case of list or dict.
print(a,type(a))
# converting list to tuple
b = tuple(y)
print(type(b))
tpl = tuple(range(1,6,2))
print(tpl)
tup =(50,60,70,80,90,100)
print(tup[0])
print(tup[-1])
print(tup[:])
print(tup[::-2]) #stepsize