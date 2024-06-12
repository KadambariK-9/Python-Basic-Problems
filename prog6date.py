'''strng=input("enter a string")
if len(strng)>=2:
    ns=strng[-1]+strng[1:-1]+strng[0]
    print("modified string :",ns)
else:
    print("string is too short.. ")


strng=input("enter a string")
wrds=strng.split()
lngst=0
for wrd in wrds:
    if len(wrd)>lngst:
        lngst=len(wrd)
print("length of the longest word:",lngst)
'''

'''
strng=input("enter the string")
cnt=0
for i in strng:
    if len(strng)>=2:
        print(strng[cnt+1])
        cnt+=1
        
strng=input("enter the string")
ns=strng[1::2]
print("modified string:",ns)
'''



'''strng=input()
while strng:
    if strng=='QUIT' or strng=='quit' or strng=='Quit':
        break
    else:
        strng=input("enter the string")
        print(len(strng))
'''
'''
while True:
    strng=input()
    if strng=='QUIT' or strng=='quit' or strng=='Quit':
        print("exiting the program")
        break
    
    print(len(strng))
'''
'''for i in range(5):
    strng=input("enter a word")
    if len(strng)<6:
        strng=input("enter a word again")

    print(strng)
'''
'''for i in range(5):
    while True:
        strng=input("enter a word")

        if len(strng)<6:
            strng=input("enter a word again")
        else: 
            print(strng)
            break


lst=[11,22,33,44,55]
for i in lst:
    print(i,end=' ')
    
lst=[11,22,33,44,55]
ind=0
while ind<len(lst):
    print(lst[ind],end=' ' )
    ind=ind+1

lst=[11,22,33,44,55]
for i,j in enumerate(lst):
    print(i,j)


lst=[11,22,33,44,55]
for i in range(len(lst)):
    print(lst[i],end=' ')
'''


'''lst=[1,2,3,4,5]
dbl_lst=[i**2 for i in lst]
print(dbl_lst)
'''

'''lst=[-12,84,11,22,-3,0,-25]
pstv_lst=[i for i in lst if i>0]
print(pstv_lst)

lst=[1,2,3,4,5,6,7]
odd_lst=[i for i in lst if i%2!=0]
print(odd_lst)
'''


'''
val=int(input("enter number of values"))
lst=[]
for i in range(val):
    ele=input(f"enter element{i+1}: ")
    lst.append(ele)
print("List:",lst)

lst=[]
ele=int(input("enter element: "))
while ele!=0:
    lst.append(ele)
    ele=int(input("enter element: "))
print("List:",lst)

n=int(input("enter length of list"))
lst=[]
for i in range(n):
    ele=input(f"enter element{i+1}: ")
    lst.append(ele)
print("List:",lst)
req=input("which side to move")
if req=='l':
    l=int(input("left side"))
    ll=lst[l:]+lst[:l]
    print(ll)
elif req=='r':
    r=int(input("right side"))
    rr=lst[-r:]+lst[:-r]
    print(rr)

n=int(input("enter length of list"))
lst=[]
for i in range(n):
    ele=input(f"enter element{i+1}: ")
    lst.append(ele)
print(" org List:",lst)
p2s=int(input("enter  number of positions to shift:"))
rr=lst[-p2s:]+lst[:-p2s]
print(f"right rotated list:{rr}")
ll=lst[p2s:]+lst[:p2s]
print(f"left rotated list:{ll}")
'''


'''
lst=[10,20,20,30,40,40,50]
unq_lst=[]
for item in lst:
    if item not in unq_lst:
        unq_lst.append(item)
print(f"original list:{lst}")
print(f"list with unique elements]:{unq_lst}")
'''
usrnm=[]
accnt=[]
lmt=[]
while True:
    print("1.Add 2.View")
    ch=int(input("Enter Choice:"))
    if ch==1:
        nm=input("Enter Name:")
        while True:
            an=int(input("Enter Account Number:"))
            can=int(input("Confirm Account Number:"))
            if an==can:
                tl=int(input("Enter Limit:"))
                usrnm.append(nm)
                accnt.append(an)
                lmt.append(tl)
                print("Beneficiary added")
                break
            else:
                print("A/c Not matched.Try again")
            print()
    elif ch==2:
        if len(usrnm)==0:
            print("List is Empty")
        else:
            print("Name\t\tAccount\t\tLimit")
            print("------------------------------------------")
            for i in range(len(usrnm)):
                print("%s\t\t%d\t\t%d"%(usrnm[i],accnt[i],lmt[i]))

    c=input("Do u want to Continue: press y/n")
    if c=='n':
        break


































    
























