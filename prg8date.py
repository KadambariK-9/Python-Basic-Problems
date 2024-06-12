'''def fn1(x):
    return x+2
def fn2(y):
    print(y)
fn2(fn1(5))

def pca(l1,l2):
    print(l1,l2)
lst=[11,22,33]
tpl=(55,66,77,)
pca(lst,tpl)

def cb(x):
    """Cube of a Number"""
    print(x**3)
print(cb.__doc__)
cb(5)


def display(name,course='BTech'):
    print("Name:"+name)
    print("course:"+course)
display(course='BCA',name='Arav')
display(name='Reyansh')

def print_it(**kwargs):
    print()
    for name,value in kwargs.items():
        print(name,value,end=' ')
print_it(a=10)
print_it(a=10,b=3.14)
print_it(a=10,b=3.14,s='Python')

def vlp_ar(*args):
    print()
    for var in args:
        print(var,end=' ')
vlp_ar(1122)
vlp_ar(1122,25.19)
vlp_ar(1122,25.19,'Python')
vlp_ar(1122,25.19,'Python','Programming')

def kw_ar(iv,fv,sv):
    print(iv,fv,sv)
kw_ar(fv=25.19,iv=1122,sv='Python')
kw_ar(sv='Python',fv=25.19,iv=1122)
kw_ar(sv='Python',iv=1122,fv=25.19)
kw_ar(s='Python',iv=1122,fv=25.19)


def details(n,r):
    print(n.upper(),r)
nm="k v"
rnk=1122
details(nm,rnk)


def details(n,r):
    print(n.upper(),r)
nm="k v"
rnk=1122
details(rnk,nm)


def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
while True:
    print("1.Add 2.Subtract 3.Multiplication 4.Division 5.Exit")
    ch=int(input("Enter Your Choice"))
    if ch==1:
        n1=int(input("Enter first number"))
        n2=int(input("Enter second number"))
        print("Sum of given numbers is :%d"%add(n1,n2))
    elif ch==2:
        n1=int(input("Enter first number"))
        n2=int(input("Enter second number"))
        print("Difference of given numbers is :%d"%sub(n1,n2))
    elif ch==3:
        n1=int(input("Enter first number"))
        n2=int(input("Enter second number"))
        print("Product of given numbers is :%d"%mul(n1,n2))
    elif ch==4:
        n1=int(input("Enter first number"))
        n2=int(input("Enter second number"))
        print("Division of given numbers is :%d"%div(n1,n2))
    elif ch==5:
        print("...........THANK YOU....................")
        break


nmbr_1=1122
def show():
    global nmbr_2
    nmbr_2=2191
    nmbr_3=22191
    print(nmbr_1)
    print(nmbr_2)
    print(nmbr_3)
show()
print(nmbr_1)
print(nmbr_2)
print(nmbr_3)

nmbr_1=1122
def show():
    nmbr_1=2191
    nmbr_2=22191
    print(nmbr_1)
    print(nmbr_2)
show()
print(nmbr_1)
print(nmbr_2)

def add(n1,n2):
    print(n1+n2)
add(12,15)

def add(n1,n2):
    sm=n1+n2
    return sm
nmbr1=float(input("Enter the first number:"))
nmbr2=float(input("Enter the second number:"))
rs=add(nmbr1,nmbr2)
print("Sum of %.2f and %.2f is %.2f"%(nmbr1,nmbr2,rs))


crd={}
for _ in range(3):
    usrnmk=input("enter username")
    pwd=input("enter a password")
    crd[usrnm]=pwd
lgn_usrnm=



import random
accnt={}
avl_bal={}
while True:
    print("1. Create A/c 2. View 3.Exit")
    ch=int(input("Enter Choice"))
    if ch==1:
        while True:
            ac_num=random.randint(100000,999999)
            if ac_num not in accnt:
                hldr_nm=input("Enter A/c Holder Name")
                blnce=int(input("Enter A/c balance"))
                accnt[ac_num]=hldr_nm
                avl_bal[ac_num]=blnce
                print("A/c created")
                break
    elif ch==2:
        if len(accnt)==0:
            print("No account")
        else:
            for i,j in accnt.items():
                print("----------------------------------------------")
                print("A/c Number\tHolder Name\tA/C Balance")
                print("----------------------------------------------")
                print('%.2d'%i,'\t\t%.2s'%j,'\t\t%.2d'%avl_bal[i])
                print("-----------------------------------------------")
    elif ch==3:
        break

        
d={}
n=int(input("enter number of persons"))
for i in range(n):
    k=input("enter username")
    v=int(input("enter a password"))
    d[k]=v
print(d)
usnm=input("enter username")
pwd=int(input("enter password"))
if usnm in d:
    if (d[k])==pwd:
        print("found")
    else:
        print("not found")
else:
    d[usnm]=pwd
    print(d)



d={}
var=input("enter string")
c=1
for i in var:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

n=int(input("enter number of items"))
for i in range(n):
    k=input("enter key")
    v=int(input("enter a value"))
    d[k]=v
print(d)

d=int(input())
d[d]=int(input())
print(d)

d={}
d['B']=int(input())
print(d)

d={}
d[75]=65
print(d)

d={}
A='A'
d[A]=65
print(d)

d={}
d['A']=65
print(d)

d={'K':11,'V':22,'S':19}
print(d.setdefault('K',25))
print(d.setdefault('Y'))
print(d.setdefault('Y',25))
      
d1={'K':11,'V':22,'S':19}
d2={'B':2,'S':19,'A':1}
print(d1,d2)
d1.update(d2)
print(d1,d2)
#d2.update(d1)
#print(d1,d2)

d={'K':11,'V':22,'S':19}
for i,(j,k) in enumerate(d.items()):
    print(i,j,k)

d={'K':11,'V':22,'S':19}
for i,j in d.items():
    print(i,j,end=' ')

d={'K':11,'V':22,'S':19}
for i in d.items():
    print(i,end=' ')


d={'K':11,'V':22,'S':19}
for i in d.values():
    print(i,end=' ')


d={'K':11,'V':22,'S':19}
for i in d:
    print(i,end=' ')


d={'K':11,'V':22,'S':19}
for i in d.keys():
    print(i,end=' ')

kys={'K','V','S'}
vls=1122
dct=dict.fromkeys(kys)
print(dct)

kys={'K','V','S'}
vls=1122
dct=dict.fromkeys(kys,vls)
print(dct)


plyrs={'p1':{'nm':'Rohit','jrsy':45},
       'p2':{'nm':'Kohli','jrsy':18},
      }
for n,j in plyrs.items():
    print(n,j)
'''
