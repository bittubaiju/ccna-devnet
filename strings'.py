a = 'bittu '
b = 'baiju'
print(a + b)
# print(a*b) # will throw error as string can only be multiplied with int
print(a[:2]+b[3:]) # [a:b] will not include b
print(a[1:-2])
print(b[-1:])
print(b[1:])
print(a[-1]) # will print nothing and also will not throw any error.
print(a[:-3]) # it will print from starting up to 1 less than -3 which in this case is t from BEHIND.
print(a[-2:]) # will start from last as it is negative index and will go till the end. so in this it will print "u"


