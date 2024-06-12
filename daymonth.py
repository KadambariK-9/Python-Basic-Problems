'''
day=int(input("enter number of days"))
y=day//365
m=(day-y*365)//30
days=(day-y*365-m*30)
print(y,"year\t ",m," month\t",days,"days")

d=730
y=int(d/365)
d=int(d%365)
m=int(d/30)
d=int(d%30)
print(y,"year",m,"month",d,"days")

n=730
y=n//365
m=n%365//30
d=n%365%30
print(y,"years",m,"months",d,"days")


m=60
d=m//(24*60)
h=d%60
m=d%h
print(d,"days",h,"hours",m,"minutes")MIN AS INPUT


x=84
n1=x//10
n2=x%10
y=(n2*10)+n1
print(y)
print(x+y)


n=40
z=n%10
r=(z*10)+(((n-z)//10))
print(r)
print(r+n)


n=60
temp=60
rev=0
rev=((temp%10)*10)+temp//10
print(rev)
x=temp+rev
print(x)


n=20
print(n+(n//10)+10*(n%10))

'''
x=120
y=10
res=x%y+x-1
print(res)

'''
x=int(input("enter the number"))
if x>250:
    x=x-40
print(x)

flag="riding car"
p=int(input())
if p>=10:
    flag="riding bus"
print("\t",flag)

flag="shut and go to scholl"
s=input()
if s=="sunday":
    flag="holiday"
print("\t",flag)    

'''































