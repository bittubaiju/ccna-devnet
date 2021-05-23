""" Since tuple is immutable so to enter a new element
at a particular position we need to slice the tuple  """
x = (10,20,30,40,50,60,70,80)
print('Tuple before inserting new element: ',x)
"""num = [int(input('enter the new element: '))]
tup = tuple(num)
pos = int(input('enter the pos: '))
x1 = x[:pos-1]
x1+=tup
x = x1+x[pos-1:]
print('new tuple is: ',x)"""

# updating a tuple element
"""num = [int(input('enter the new element: '))]
tup = tuple(num)
pos = int(input('enter the pos: '))
x1 = x[:pos-1]
x1 += tup
x = x1+x[pos:]
print('new tuple is: ',x)"""

# deleting a tuple element
pos = int(input('enter the pos element you want to delete: '))
x1 = x[:pos-1]
x = x1+x[pos:]
print('new tuple is: ',x)
