# list comprehension is a compact code which performs the action.
#syntax looks like: [exp for item1 in interable condition if any]

sqr = [x**2 for x in range(1,11)] # compact code
print(sqr)
even_sqr = [x**2 for x in range(1,11) if x%2==0] # compact
print(even_sqr)
# OR
even_sqr1 = [x**2 for x in range(2,11,2)] # even more compact
print(even_sqr1)

# adding elements of list
x = [1,4,5,6,7]
y=[10,40,35,32]
lst=[]
for i in x:
    for j in y:
        lst.append(i+j)
print(lst)
# OR
lst = [i+j for i in x for j in y] #compact code list comprehension
print(lst)
lst = [i+j for i in 'ABC' for j in 'DE'] # adding letters
print(lst)
# displaying the 1st letters of the word.
fruits = ['Apple','Orange','Banana','Mango']
frt = []
for i in fruits:
    frt.append(i[0])
print(frt)
#OR
frt =[i[0] for i in fruits] # compact form of the above code.
print(frt)
