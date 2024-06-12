'''l=[4,0,5,0,1,9,0,0]
n=int(input('enter no of elements'))
i=0
j=0
for i in range(n):
    if l[i]!=0:
        l[j]=l[i]
        j=j+1
while j<n:
    l[j]=0
    j=j+1
print(l)
'''
'''output
enter no of elements8
[4, 5, 1, 9, 0, 0, 0, 0]
'''

'''
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n1=int(input('num'))
res=fact(n1)
print(res)

num5
120



def f(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return f(n-1)+f(n-2)
n1=int(input('num'))
res=f(n1)
print(res)




def pow(n,m):
    print(n**m)
n1=int(input('enter 1 no'))
m1=int(input('enter 2 no'))
pow(n1,m1)


def p(n,m):
    if m==0:
        return 1
    else:
        return n*p(n,m-1)
n1=int(input('enter 1 no'))
m1=int(input('enter 2 no'))
res=p(n1,m1)
print(res)



enter 1 no5
enter 2 no2
25



def sum(n):
    if n==0:
        return 0
    return n%10+sum(n//10)
n1=int(input('enter num'))
res=sum(n1)
print(res)

'''




'''def __init__(self):
        self.s=20
obj=cse1()



class cse1:
    def __init__(self,a,b):                    
        self.a1=a
        self.b1=b                                
    def strength(self):
        print('strength is myself')
        self.s=101
    def ks(self,c,d):
        print("KS")
        self.k='good'
        p=c*d
        print(p)
    def details(self):
        print('strength and ks')
        c_s=self.s-10
        print(c_s,self.k)
        print(self.a1+self.b1)
obj=cse1(4,5)
obj.strength()
obj.ks(2,3)
obj.details()


strength is myself
KS
6
strength and ks
91 good
9




class Faculty:
    def __init__(self,f_name,dep,f_id):
        self.f_name==f_name
        self.dep=dep
        self.f_id=f_id
    def print_info(self):
        print('faculty information=',self.f_name,self.dep,self.f_id)
obj=Faculty('khush','cs',1001)
obj.print_info()



class Cse(Faculty):
    pass
obj1=Cse("jyothi mam",'cs',1002)
obj1.print_info()






class a:
    def __init__(self):
        print('it is class a ')
        self.n=5
        self.m=4
class b(a):
    def bb():
        print('it is class b')
        print(n*m)
        self.n1=self.n*self.m
class c(b):
    def cc(self):
        print('it is class c')
        print(self.n1)
#obja=a()
#objb=b()
#objb.bb()
objc=c()
objc.cc()






class father:
    def __init__(self,n1):
        print('it is father class')
        self.n=n1
class mother:
    def __init__(self,m1):
        print('it is mother class')
        self.m=m1
class child(father,mother):
    def __init__(self):
        print('child class')
        print(self.n*self.m)

obj1=father(2)
obj2=mother(3)
obj3=child()



class A:
    def __init__(self,n,m):
        print("grandfather class")
        self.n=n
        self.m=m
class B(A):
    def __init__(self):
        print("father class")
        print(self.n)
class C(A):
    def __init__(self):
        print("child class")
        print(self.m)
a=A(2,3)
b=B()
c=C()



in python method overloading and constructer overloading not possible but possible in operator overloading
function and constructer over ridding is possible 



j=0
a=[2,1,0,1,1,2,0,0]
c_0=0
c_1=0
c_2=0
for i in range(len(a)):
    if a[i]==0:
        c_0=c_0+1
    elif a[i]==1:
        c_1=c_1+1
    else:
        c_2=c_2+1
while c_0>0:
    a[j]=0
    j=j+1
    c_0=c_0-1
while c_1>0:
    a[j]=1
    j=j+1
    c_1-=1
while c_2>0:
    a[j]=2
    j=j+1
    c_2-=1
print(a)

[0, 0, 0, 1, 1, 1, 2, 2]


CREATE A CLASS CAR SHOW ROOM IN WHICH
1. CREATE A FUNCTION NAME CAR COMPANY WHICH WILL
ALLOW USER TO SELECT A CAR COMPANY OUT OF THE
DISPLAYED COMPANY.IF THE USER ENTERS ANY RANDOM
CAR COMPANY HE / SHE SHOULD BE ASKED TO REENTER.
2. ACCORDING TO THE CAR COMPANY SELECTED THE
USER SHOULD BE REDIRECTD TO SELECTING THE
COMPANY MODELS OF THAT COMPANY OUT OF THE GIVEN
LIST.
3. AFTER SELECTING THE MODEL THE USER SHOULD BE
REDIRECTED TO SELECTING THE VARIANT(PETROL/DieseL)
4. ACCORDING TO THE CAR COMPANY MODEL AND VARIANT
A PRICE SHOULD BE CALCULATED TO WHICH SGST AND
CGST ARE ADDED TO MAKE IT THE TOTAL PRICE.
NOTE: SGST(STATE) AND CGST(CENTRAL) ARE COMMON
FOR ALL THE CARS.

'''

class Car:
    def select(self):
        sgst_t1=100
        cgst_t1=150
        sgst_t2=200
        cgst_t2=350
        sgst_b1=200
        cgst_b1=350
        sgst_b2=400
        cgst_b2=550
        total=0
        petrol=500
        diesel=750
        while True:
            print('1.TATA \n 2.BMW \n 3. SUZUKI \n 4. MARUTHI \n')
            ch1=input('ENTER WHICH COMPANY YOU WANT MADAM')
            if ch1.lower()=='tata':
                print('1. TATA MODEL1 \n 2. TATA MODEL2')
                tm=input('enter the model of tata company:')
                if tm.lower()=='tata_model1':
                      print('select the variant:\n 1. petrol \n 2. diesel')
                      tv=input('enter a variant')
                      if tv.lower()=='petrol':
                          total=sgst_t1+cgst_t1+petrol
                          print('THANK YOU MAM FOR PURCHASE \n THE TOTAL COST IS ',total)
                      elif tv.lower()=='diesel':
                          total=sgst_t1+cgst_t1+diesel
                          print('THANK YOU MAM FOR PURCHASE \n THE TOTAL COST IS ',total)
                elif tm.lower()=='tata_model2':
                      print('select the variant:\n 1. petrol \n 2. diesel')
                      tv=input('enter a variant')
                      if tv.lower()=='petrol':
                          total=sgst_t2+cgst_t2+petrol
                          print('THANK YOU MAM FOR PURCHASE \n THE TOTAL COST IS ',total)
            elif ch1.lower()=='bmw':
                print('1. BMW MODEL1 \n 2. BMW MODEL2')
                bm=input('enter the model of bmw company:')
                if bm.lower()=='bmw_model1':
                      print('select the variant:\n 1. petrol \n 2. diesel')
                      bv=input('enter a variant')
                      if bv.lower()=='petrol':
                          total=sgst_b1+cgst_b1+petrol
                          print('THANK YOU MAM FOR PURCHASE \n THE TOTAL COST IS ',total)
                      elif bv.lower()=='diesel':
                          total=sgst_b1+cgst_b1+diesel
                          print('THANK YOU MAM FOR PURCHASE \n THE TOTAL COST IS ',total)
                elif bm.lower()=='bmw_model2':
                      print('select the variant:\n 1. petrol \n 2. diesel')
                      bv=input('enter a variant')
                      if bv.lower()=='petrol':
                          total=sgst_b2+cgst_b2+petrol
                          print('THANK YOU MAM FOR PURCHASE \n THE TOTAL COST IS ',total)
            else:
                print('MADAM THIS COMPANY DOES NOT EXIST !... \n PLEASE TRY ANAGIN')
                break
        
obj=Car()
obj.select()


class car:
    def __init__(self):
        self.cgst=5555
        self.sgst=5555
        self.insurance=5555
    def company(self):
        while True:
            print('Toyota,Mercedes')
            self.n=input('enter the car company')
            if self.n=='Toyota':
                print('welcome to toyo')
                




                      '''find the next greater value for every element
                      [14,2,16,4,3,5]

''













