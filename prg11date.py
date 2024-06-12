class Vehicle:
    def wheels(self):
        pass
class Cycle(Vehicle):
    def wheels(self):
        return 'two'
class Auto(Vehicle):
    def wheels(self):
        return 'three or four'
class Car(Vehicle):
    def wheels(self):
        return 'four'
def dsply(Vehicle):
    return Vehicle.wheels()
cy=Cycle()
at=Auto()
cr=Car()
print(dsply(cy))
print(dsply(at))
print(dsply(cr))

'''class bs1():
    def dsp11(self):
        print("Welcome to Class1")
class bs2():
    def dsp12(self):
        print("Welcome to Class2")
class derived(bs1,bs2):
    def dsp13(self):
        print("Welcome to  Derived Class")
emp=derived()
emp.dsp11()
emp.dsp12()
emp.dsp13()


class College():
    def clg(self):
        print("College: BITM  ")
class Department(College):
    def dept(self):
        print("Department:  CSE      ")
class Designation(Department):
    def dsgn(self):
        print("Designation:    STUDENT     ")
emp=Designation()
emp.clg()
emp.dept()
emp.dsgn()
    
class College():
    def __init__(self,name,age):
        self.nm=name
        self.ag=age
    def dsply(self):
        print(self.nm,self.ag)
class Student(College):
    pass
s1=Student('SK',33)
s1.dsply()


class ABC:
    def __init__(self,var):
        self.var=var
    def dsply(self):
        print('var is=',self.var)
    def print(self):

        self.var+=2
        self.dsply()
obj=ABC(10)
obj.print()


class ABC:
    def __init__(self,var1,var2):
        self.var1=var1
        self.__var2=var2
    def dsply(self):
        print('From class method,var1=',self.var1)
        print('From class method,var2=',self.__var2)
obj=ABC(10,20)
obj.dsply()
print('From main module,var1=',obj.var1)
print('From main module,var2=',obj._ABC__var2)


class Emp:
    def __init__(self,nm,id):
        self.name=nm
        self.__eid=id
    def __dsply(self):
        print(self.name,self.__eid)
e1=Emp('S K',1122)
print(e1.name)
e1._Emp__dsply()
print(e1._Emp__eid)

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f'({self.x},{self.y})'
def midpoint(p1,p2):
    mx=(p1.x+p2.x)/2
    my=(p1.y+p2.y)/2
    return Point(mx,my)
p=Point(-2,1)
q=Point(5,4)
r=midpoint(p,q)
print(str(r))




class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f'({self.x},{self.y})'
    def midpoint(p1,p2):
        mx=(p1.x+p2.x)/2
        my=(p1.y+p2.y)/2
        return Point(mx,my)
p=Point(-2,1)
q=Point(5,4)
r=p.midpoint(q)
print(str(r))

'''
'''class point1:
    def __init__(self,x,y):
        self.x1=x
        self.y1=y
    def midpoint(self):
        return '%.1f'%((self.x1+self.y1)/2)
p1=point1(-2,5)
mp1=p1.midpoint()
print(f"Average is {mp1}")
class point2:
    def __init__(self,x,y):
        self.x2=x
        self.y2=y
    def midpoint(self):
        return '%.1f'%((self.x2+self.y2)/2)
p2=point2(1,4)
mp2=p1.midpoint(p2)
print(f"Average is {mp2}")

m=mp1,mp2
print(f'mid {m}')


class Cirle:
    pi=3.14159
    def __init__(self,r):
        self.radius=r
    def area(self):
        return self.pi*self.radius**2
c1=Circle


class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def reflect_x(self):
        return Point(self.x,-self.y)
    def __str__(self):
        return f"Point({self.x},{self.y})"
op=Point(3,5)
rp=op.reflect_x()
print(f'Original Point:{op}')
print(f'Refelcted Point:{rp}')
'''
