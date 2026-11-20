'''
class student:
    name="Aaa"
    age=20
s1=student()
s2=student()
s1.name="ABC"
s2.name="DEF"
print(s2.name)
print(s1.name)
print(student.name) '''


#creating Object.nj

'''
class college:
    name='GCEM'
    location="Hoodi"    

    @classmethod #additional object, public access method
    def disp(cls):
        print(cls.name,cls.location)

    def __init__(self,name,age,dept):  #init means initialization
        self.name=name
        self.age=age
        self.dept=dept
    def display(self):
        print(self.name,self.age,self.dept)
    def change_name(self,new):  #if u want to change names
        self.name=new
    def change_dept(self,new):
        self.dept=new
s1=college("Aaa",20,"CSE")
s2=college("Bbb",23,"AIML")
s3=college("Ccc",22,"CSE")
s2.change_name("Ddd")
s3.change_dept("AIML")
s1.display()
s2.display()
print('_-_-_-_-_-_-_-_-_')
s3.display()
'''

'''
class A:
    a=10
class B(A):
    b=20
ob1=B()      #can't access parent class properties
print(ob1.a,ob1.b)

'''

'''class Bank:
    bname='CANARA'
    bloc='CNRB'

    def __init__(self,name,phno,eid):
        self.name=name
        self.phno=phno
        self.eid=eid
    def display(self):
        print(self.name,self.phno,self.eid,end=' ')
c1=Bank("Aaa",7338574477,"c@gmail.com")
class Bank_details(Bank):
    founder='SaiRam'

    def __init__(self,name,phno,eid,add,pan):
        super().__init__(name,phno,eid) #super method will work as chain it connects parent and child
        self.add=add
        self.pan=pan
    def display(self): 
        super().display()
        print(self.add,self.pan)
c1=Bank_details("Aaa",7338574477,"c@gmail.com","Bglr","wxz345838")
c1.display()'''


#multi level inheritance

'''class A:
    a=10
class B(A):
    b=20
class C(B):
    c=30
class D(C):
    d=40
ob1=D()
print(ob1.a,ob1.b,ob1.c,ob1.d)
'''
'''class school:
    sname='ABC'
    sloc='E.city'
 
class college(school):
    cname='GCEM'
    cloc='Hoodi'
class Masters(college):
    uname='Jain'
    uloc='BSVM'
    
    @classmethod
    def display(cls):
        print(cls.sname,cls.sloc,cls.cname,cls.cloc,cls.uname,cls.uloc)
Masters.display()    
'''

#Multiple Inheritence
'''class school:
    sname='ABC'
    sloc='E.city'
 
class college(school):
    cname='GCEM'
    cloc='Hoodi'
class Masters(college,school):
    uname='Jain'
    uloc='BSVM'
    
    @classmethod
    def display(cls):
        print(cls.sname,cls.sloc,cls.cname,cls.cloc,cls.uname,cls.uloc)
Masters.display()  
print(Masters.mro())  #Method Resolution Order
'''


#Hierarchical Inheritance

'''class school:
    sname='ABC'
    sloc='E.city'
 
class college(school):
    cname='GCEM'
    cloc='Hoodi'
s1=college()
print(s1.sname)
class Masters(school):
    mname='GCE'
    mloc='Bglr'
s2=Masters()
print(s2.sname)'''


#Hybrid Inheritance

'''class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

class TeachingAssistant(Student, Teacher):
    def __init__(self, name, course, subject):
        Person.__init__(self, name)
        self.course = course
        self.subject = subject

    def display(self):
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Subject: {self.subject}")

ta = TeachingAssistant("Anu", "Python", "Programming")
ta.display()

print("Method Resolution Order:", TeachingAssistant.mro())'''


#Polymorphism

'''class Demo:
    @staticmethod
    def sam():
        print("This is static method")
            
    @staticmethod
    def add(a,b):
        print(a+b)
        
    @staticmethod
    def multiply(a,b,c):
        print(a+b+c)
        
ob=Demo()
ob.sam()
ob.add(10,20)
ob.multiply(10,20,30)   
'''

'''
class Demo:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return Demo(self.value+other.value)
a=Demo(100)
b=Demo(200)

c=a+b
print(c.value)

print("-------Concatenation-------")

s1=Demo("Hi")
s2=Demo("Guys")
result=s1+s2
print(result.value,type(result.value))
'''
     
#Encapsulation

'''class Bank:
    __deposit=1000
    def __init__(self,name,phno,acc_no):
        self.name=name
        self.phno=phno
        self.__acc_no=acc_no #private variable
        
b=Bank("Aaa",7338574477,1234567890)
print(b.name)
print(b.phno)
print(b._Bank__acc_no) #(obj._cname_vae/method)
print(Bank._Bank__deposit) #(cname._cname__var/method)
Bank.___deposit=2000000000
print(Bank._Bank__deposit)
'''

class Bank:
    def __init__(self,name,bal):
        self.name=name
        self.__bal=bal #private variable
        
    def get_balance(self):
        return self.__bal
    
    def set_bal(self,amount):
        self.__bal=amount
        
    #deposit
    
    def deposit(self,amount):
        self.set_bal(self.get_balance()+amount)
        
    #withdraw
    
    def withdraw(self,amount):
        if amount <=self.get_balance():
            self.set_bal(self.get_balance()-amount)
        else:
            print("Insufficient balance")

b=Bank("ABC",10000)
print("-----Before-----")
print(b.get_balance())
print("------After-------")
b.deposit(5000)
print(b.get_balance())
b.withdraw(3000)
print(b.get_balance())