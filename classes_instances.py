#INSTANCES == OBJECTS

class Employee:
    pass
#instances of Employee:
e1=Employee()
e2=Employee()

print(e1)
print(e2)

e1.name="Binayak"
e1.email="binayak@gmail.com"
e1.roll=20

e2.name="Bishnu"
e2.email="bishnu@gmail.com"
e2.roll=21

print(e1.name)
print(e2.name)


#with constructor
print("\nwith constructor")
class Employee_1:
    def __init__(self,name,roll): #called methods in python
        self.name=name
        self.roll=roll
        self.email=name + '@gmail.com'
    
    def nameroll(self):
        print("{} {}".format(self.name,self.roll))

e1_1=Employee_1("Binayak",20) #called instance
e2_1=Employee_1("Bishnu",40)

print(e1_1)
print(e2_1)

print(e1.name)
print(e2.name)

e1_1.nameroll()
e2_1.nameroll()

Employee_1.nameroll(e1_1)

#=======================================
#class variables:
print("\nwith class variables")
class Employee_2:

    no_emp = 0
    x = 1

    def __init__(self,name,roll): #called methods in python
        self.name=name
        self.roll=roll
        self.email=name + '@gmail.com'
        Employee_2.no_emp +=1 #not required to use self
                            #since does not change with different instances
    
    def nameroll(self):
        print("{} {}".format(self.name,self.roll))

    def updateroll(self):
        print("from {} to {}".format(self.roll,self.roll+self.x)) #self required even for x

e1_2=Employee_2("Binayak",20) #called instance
e2_2=Employee_2("Bishnu",40)

e1_2.nameroll()
e1_2.updateroll()
'''
print(e1_2.__dict__)
print(Employee.__dict__)
print(Employee_1.__dict__)
print(Employee_2.__dict__)
'''

#Employee_2.x = 2
e1_2.x=2
e1_2.updateroll()
e2_2.updateroll()

print("\n{}".format(Employee_2.no_emp))

#========================================
#class method:
print("\nwith class method")
class Employee_3:

    no_emp = 0
    x = 1

    def __init__(self,name,roll): #called methods in python
        self.name=name
        self.roll=roll
        self.email=name + '@gmail.com'
        Employee_2.no_emp +=1 #not required to use self
                            #since does not change with different instances
    
    def nameroll(self):
        print("{} {}".format(self.name,self.roll))

    def updateroll(self):
        print("from {} to {}".format(self.roll,self.roll+self.x))

    @classmethod    #decorator
    def set_updateroll(cls,amount): #takes class not instance (self) as 1st variable
        cls.x = amount

    #part_2
    @classmethod
    def from_str(cls, s):
        n,r=s.split('-')
        return cls(n,r)

e1_3=Employee_3("Binayak",20) #called instance
e2_3=Employee_3("Bishnu",40)

Employee_3.set_updateroll(4)    #equivalent to
                                #Employee_3.x = 4
                                #changes for all instances
#also:
#e1_3.set_update(4)  #changes all and not only instance

e1_3.nameroll()
e1_3.updateroll()
print(Employee_3.x)
print(e1_3.x)

#part_2
#to take inputs of elements from string

#usual
s="Binayak-40"
n,r = s.split('-')
e3_3 = Employee_3(n,r)
e3_3.nameroll()

#alternative...use class method
s1="Bishnu-50"
e4_3 = Employee_3.from_str(s1)
e4_3.nameroll()

'''
#other class mathods:
class datetime:
    @classmethod
    def today(cls):
        t = _time.time()
        return cls.fromtimestamp(t)
    
    @classmethod
    def fromtimestamp(cls,t):
        y,m,d,hh,mm,ss,weekday,jday,dst = _time.localtime(t)
        return cls(y,m,d)
        '''

#======================================================
#calling one function from another in class: (own idea)
print("\nImplicit function calling")
class abc:
    x = 0
    def getval(self,n):
        self.x = n
        self.putval()

    def putval(self):
        print(self.x)

A = abc()
A.getval(30)

#========================================
#static method:
print("\nStatic method-datetime")
import datetime
class defg:
    @staticmethod
    def dayofweek(day):
        if day.weekday() == 5  or day.weekday() == 6: 
            #monday==0.....sunday==6
            return "Weekend"
        return "Weekday"

date_ = datetime.date(2021,1,22)
print(date_)
print(defg.dayofweek(date_))

#=============================================
#inheritance/subclasses:
print("\nInheritance + subclasses:")
class Employee_4:

    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first.lower() + '.' + self.last.lower() + '@gmail.com'

    def fullname(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee_4):
    #pass
    raise_amount = 1.10
    
    #part-2
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay) #employee handles these
        #Employee.__init__(self,first,last,pay) #alternative
        self.prog_lang = prog_lang

#part-3
class Manager(Employee_4):
    def __init__(self,first,last,pay,employees=0):  #did not pass as list originally
        #better not to pass mutable datatypes but form inside
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = [] #list formed (empty)
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        
    def print_emp(self):
        for emp in self.employees:
            print('-',emp.fullname())

'''
dev_1 = Employee_4('Corey','Spencer',50000)
dev_2 = Developer('Sam','Linn',50000)

# print(help(Developer))

print(dev_1.email)
print(dev_2.email)

print(dev_1.pay)    #from employee
dev_1.apply_raise()
print(dev_1.pay,dev_1.raise_amount)
print(dev_2.pay)    #from developer
dev_2.apply_raise()
print(dev_2.pay,dev_2.raise_amount)
'''
#part-2
dev_3 = Developer('George','Plac',50000,'Python')

print(dev_3.email)
print(dev_3.prog_lang)

#part-3
mgr_1 = Manager('Sue','Smith',90000,[dev_3])

print(mgr_1.email)
mgr_1.print_emp()

print('\nAdding dev_2')
dev_2 = Developer('Sam','Linn',50000,'C++')
mgr_1.add_emp(dev_2)
mgr_1.print_emp()

print("\nRemoving dev_3")
mgr_1.remove_emp(dev_3)
mgr_1.print_emp()

print()
print(isinstance(mgr_1,Manager))
print(isinstance(mgr_1,Employee_4))
print(isinstance(mgr_1,Developer))

print()
print(issubclass(Developer,Manager))
print(issubclass(Manager,Employee_4))
print(issubclass(Developer,Employee_4))

#===============================================
#special methods
print("\nMagic/Dunder methods:")
class Employee_5:
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first.lower() + '.' + self.last.lower() + '@gmail.com'

    def fullname(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self): #mainly for debugging and logging
        return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)
        #also good for debugging and logging
        #overwrites above __repr__

    def __add__(self,other): #other is for taking another object of same class
        return self.pay + other.pay #to add pay
        #return self.fullname() + ' ' + other.fullname() #to add names

    
def __len__(self):
        return len(self.fullname())

dev_1 = Employee_5('Corey','Spencer',50000)
dev_2 = Employee_5('Sam','Linn',50000)

print(dev_1)    #not really user friendly
#but after defining __repr__ prints like we want without calling
#like __init__ constuctor
#similiarly for __str__
print()
print(repr(dev_1))
print(str(dev_1))
print()
print(dev_1.__repr__())
print(dev_1.__str__())

print(1+2)  #is actually using special method
            #called dunder add inside int class
print(int.__add__(1,2)) #same output
print('a'+'b')
print(str.__add__('a','b'))
#but __add__ can be user defined in class to defined based on program
print(dev_1 + dev_2) #will give error 
                        #system define __add__ does not take
                        #employee_5 objects...only system defined objects
                        #like int, str
#error not shown after defining in class
###'see enumerating types' documentation for similiar examples

print(len(dev_1.fullname()))
print(dev_1.fullname().__len__()) #works without declaraction in class
#since inbuilt method but can be redefined as a class method

