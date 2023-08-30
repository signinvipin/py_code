## Object Oriented programming with Python

# Create class object
# Create instance
# Create new object inheriting class object - Inheritance


print('>>> Class Object <<<')

'''
print('>> Class Calling Constructor/Destructor <<')
# Destructor is seldom used. Constructor is mostly called.
class planet ():
    x = 0

    def __init__ (self,):
         print('Called constructor')

    def count (self,):
        self.x = self.x + 1
        print('So far',self.x)

    def __del__ (self,):
        print('Called destructor')

# instance planetCount created, constructor called
planetCount = planet()
planetCount.count()
planetCount.count()
planetCount.count()
# instance planetCount destructed after use of it finished
'''

'''
print('>> Creating Different Instances <<')
'''

'''
class science ():
    rollNum = 0
    name = ''

    def register (self,x):
        self.name = x
        self.rollNum = self.rollNum + 1
        print('name',self.name,'& roll number',self.rollNum)
'''

'''
# create Instances
student = science()

# calling methods and fields from instance
student.register('Jack')
student.register('Fruit')
student.register('Cauli')
student.register('Flower')
'''
'''
print('Create Child Class')

class scienceLab (science):
    lab = ''
    def assignLab (self,x,nam):
        self.lab = x
        self.register(nam)
        print('Lab',self.lab)

labassign = scienceLab()
labassign.assignLab('Chemistry', 'Methane')
labassign.assignLab('Physics', 'Spectrum')
labassign.assignLab('Biology', 'Spore')
'''
