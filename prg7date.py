'''st={11,22,33,44,55}
for i,j in enumerate(st):
    print(i,j)


st={11,22,33,44,55}
for i in st:
    print(i,end=' ')


import random
opn_bal=5000
avl_bal=opn_bal
accnt=12345
trnsctn=()
while True:
    print("1.to do transaction 2.view 3. exit")
    ch=int(input("enter choice"))
    if ch==1:
        ty=input("Transcation deposit/withdraw:D/W")
        if ty.upper()=='D':
            amt=int(input("Enter Deposit amount: "))
            avl_bal=avl_bal+amt
            t_id=random.randint(100000,999999)
            trnsctn=trnsctn+((t_id,accnt,ty,amt,avl_bal),)
            print("Deposit Done")
        elif ty.upper()=='W':
            amt=int(input("Enter Withdraw amount:"))
            if amt<avl_bal:
                avl_bal=avl_bal-amt
                t_id=random.randint(100000,999999)
                trnsctn=trnsctn+((t_id,accnt,ty,amt,avl_bal),)
                print("Withdraw Done")
            else:
                print("Insufficiant Balance....Try again")
    elif ch==2:
        if len(trnsctn)==0:
            print("No Transaction")
        else:
            for i in trnsctn:
                print("------------------------------------------------")
                print("-------------------Dteails----------------------")
                print("------------------------------------------------")
                print("T_ID\tA\C No.\tType Amount\tAvailable Balance")
                print("%d\t%d\t%s\t%d\t%d"%(t_id,accnt,ty,amt,avl_bal))
                #print(*i,"\t")
                print("-------------------------------------------------")
    elif ch==3:
        print("..........Exiting Program.......")
        break




tp1=()
n=int(input("Enter no. of elements in tuple:"))
for i in range(n):
    ele=int(input())
    tp1=tp1+(ele,)
print(tp1)

lst=[1,2,3,4,5]
dtp1=tuple(i for i in lst if i%2==0)
print(dtp1)

lst=[1,-2,3,-4,5]
dtp1=tuple(i for i in lst if i>0)
print(dtp1)

lst=[1,2,3,4,5]
dtp1=tuple(i**2 for i in lst)
print(dtp1)

plyrs=["Kohli","Rohit"]
jrsys=[18,45]
tm=list(zip(plyrs,jrsys))
print(tuple(tm))
print(list(tm))

tp1=(11,22,33,44,55)
for i,j in enumerate(tp1):
    print(i,j)

tp1=(11,22,33,44,55)
for i in range(len(tp1)):
    print(tp1[i],end=' ')

tp1=(11,22,33,44,55)
ind=0
while ind<len(tp1):
    print(tp1[ind],end=' ')
    ind=ind+1

tp1=(11,22,33,44,55)
for i in tp1:
    print(i,end=' ')
'''
