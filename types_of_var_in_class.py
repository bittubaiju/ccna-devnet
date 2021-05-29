""" 2 types of variables written inside class
1.instance variable
2.class variable"""
# Instance variable: Separate copy is created in every instance.
'''class Employee:
    def __init__(self):
        self.name = "Bittu"
        self.designation = "Software Engineer"
    def emp_detail(self):
        print("Name of the emp: ",self.name)
        print("Designation is: ",self.designation)
    def promotion(self,m = " "):
        self.designation = m
        print("Designation is: ", self.designation)

e1 = Employee()
print(e1.emp_detail())
e2 = Employee()
print("\nAfter Promotion")
e2.promotion("Senior Software Engineer")'''
'''class Modify:
    def __init__(self):
        self.x = 10
    def modify(self):
        self.x+=1
m1 = Modify()
print(m1.x)
m1.modify()
print(m1.x) #m1.x value is changed but did not effect m2.x. these are called instanse variable
m2 = Modify()
print(m2.x)'''
# Class variable: Single copy is available to all the instances
class Sample:
    x = 10 #class variable
    @classmethod #to tell the class that below method is a class method
    def modidy(cls): # class method, will by default take cls
        cls.x+=1

s1 = Sample()
s2 = Sample()
print('print S1: ',s1.x)
print('print S2: ',s2.x)
# After modify
s1.modidy() #we modified s1 but we see that even s2's instance variable also changed.
print('print S1: ',s1.x)
print('print S2: ',s2.x)




