# constructor is used to initilise the instance variables.

class Student:
    def __init__(self,name = " ",age = 0,study = 'nothing' ): #default values.
        self.name = name
        self.age = age
        self.study = study
    def speak(self):
        print("what is your name: ",self.name)
        print("what is your age: ",self.age)
        print("what are you studying: ",self.study)

s1 = Student() #constructor will be initilized with default instance variable values
print(s1.name)
print(s1.age)
print(s1.study)
s2 = Student('Bittu',24) # for name and age, contructor take values from here and for study will take default value
print(s2.name)
print(s2.age)
print(s2.study)
print(s2.speak())
''' in this code constructor will be called twice, because 2 instances are created for student class'''
