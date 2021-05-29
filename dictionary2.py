# program to print keys, value and then key value
'''dict = {'name':'Bittu','age':24,'gender':'Male'}
print(dict)
print('keys in dict: ',dict.keys())  #will print only keys, return: tuple of list
print('value in dict: ',dict.values()) #will print only value, return: tuple of list
print('key value combination: ',dict.items())#will print whole dict,return:tuple of list where each key:value is a tuple'''

#to find the sum of the values.
"""dict = {'A':12,'B':23,'C':43,'D':65}
sum1 = sum((dict.values()))
print(sum1)
# dictionary don't have append func, so we will use update func to add the elements"""
x = dict()  # or x = {} empty dict
print('how may elements: ',end='')
n= int(input())
for i in range(n):
    print('Enter the key: ',end='')
    k = input()
    print('enter the value: ',end='')
    v=int(input())
    x.update({k:v}) #storing the value of key value in dict x using update func
print(x)
