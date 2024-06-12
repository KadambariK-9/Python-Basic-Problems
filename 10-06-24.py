'''CALCULATE THE SUM OF DIGITS OF A NUM WHERE
EACH DIGIT IS POWERED TO NO OF DIGITS IN THAT
NUMBER

sz=int(input('enter length of number'))
n=int(input('enter number'))
sum=0
tmp=n
for i in range(sz):
    n=n%10
    sum=sum*10+n
    n=n//10
print(n)
print(sum)
print(n**3)


n=int(input('enter no:'))
temp=n
org=n
count=0
ans=0
while n>0:
    count=count+1
    n=n//10
while temp>0:
    dig=temp%10
    p=dig**count
    ans=ans+p
    temp=temp//10
    print(ans)
if ans==org:
    print('arm')
else:
    print('no')



n=int(input('enter no:'))
temp=n
org=n
count=0
ans=0
while n>0:
    count=count+1
    n=n//10
while temp>0:
    dig=temp%10
    p=dig**count
    count=count-1
    ans=ans+p
    temp=temp//10
    print(ans)
if ans==org:
    print('arm')
else:
    print('no')
    
//multiplying number with index
value and adding it



* * * *
*     *
*     *
* * * *
for i in range(4,1,-1):
    for j in range(1):
        print('*')
    print('\t')
    print('*')
print('\t')        


inp=input('coordinates:')
a=('a','b','c','d','e','f','g','h')
for i in range(8,1):
    print(a[i])
    for j in range(8,2):
        print('*')
    print(a[i],j)







e_r='2468'
o_r='1357'
e_c='bdfh'
o_c='aceg'
s='h6'
if s[0] in e_c:
    if s[1] in e_r:
        print('b')
    else:
        print('w')
else:
    if s[1] in e_r:
        print('w')
    else:
        print('b')



c=10
n=6
s=int(input('enter start position'))
a=(s+c-1)%n
if a==0:
    print(n)


if s is

n=6
print(n for i in range(6) if i%n==0)

'''


'''write a program to build a login system using functions.
the function name shuld be login and register
i. it should ask user to enter the details for registration
and out off all these details only username and password should be stored.
ii. now this fun shd ask user to enter usrname and password.
if these match with the registered details login success otherwise repeat
the login process saying invalid details until they are right. '''


def register():
    d={}
    usr_name=input("enter the name to regiter")
    passwd=input("enter the password for register")
    d[usr_name]=passwd
    while True:
        name=input("enter the name")
        pswd=input("enter the password")
        if name in d:
            if d[name]==pswd:
                print('login successfull')
                break
            else:
                print('invalid try again')
        else:
            print('user doesnt exist')
            break 
register()

