class student:
    name = "ram"
    age = 20
s1=student()
s2=student()

s1.name="Ramu"
s2.name="Shiva"
print(s1.name)
print(s2.name)
print(student.name)




...

class college:
    name = 'Gopalan University'
    loc = 'Hoodi'

    @classmethod
    def disp(cls):
        print(cls.name, cls.loc)
    @classmethod
    def change_loc(cls, new):
        cls.loc = new

    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept

    def display(self):
        print(self.name, self.age, self.dept)
    def change_name(self, new):
        self.name = new

s1 = college("Raju", 20, "CSE")
s2 = college("Ramu", 21, "ECE")
print("Before")
s2.display()
s2.change_name("Rama")
print("after")
s2.display()
print('----------------')
college.change_name(s1, "Raj")
college.display(s1)
print(s1.name)
print('----------------')

s1.disp()

s2.disp()

college.change_loc("Bangalore")
college.disp()

print(s1.loc)
