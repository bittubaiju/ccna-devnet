'''
class contains attributes and action which are common among a group.
where attributes are variables and actions are methods.'''
class student: #by defualt will 'object as base class'
    def __init__(self): # constructor
        self.name = 'Bittu' #initilizing the variables
        self.age = 24
        self.gender = 'Male'
    def talk(self):
        print('My name is',self.name) #calling instance variable throug instance method
        print('My age is ',self.age)
        print('my gender is ',self.gender)

s1 = student()
print(s1.talk())
