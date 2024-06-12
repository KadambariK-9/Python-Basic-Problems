'''def creatn():
     print("*************************************") 
     print("\n ACCOUNT CREATION ")
     print("\n*************************************") 
     print("\nYour Account Number is :%d",i)
     no = i
     s[a].name=input("\nEnter your Name:") 
     print("\nYour Deposit is Minimum Rs.500") 
     s[a].dep=500 
     a=a+1
     i+=1 
                    
def depst():
    no
    b=0
    m=0 
    printf("*************************************")
    printf(" DEPOSIT ")
    printf("*************************************")
    printf("Enter your Account Number")
    for b in range(b<i): 
        if(s[b].no == no): 
            m = b
            if(s[m].no == no): 
                print(" Account Number : %d",s[m].no) 
                print(" Name : %s",s[m].name)
                print("Deposit : %f",s[m].dep) 
                aa=int(input("\n How Much Deposited Now:")) 
                s[m].dep+=aa
                print("Deposit Amount is :%f",s[m].dep) 
            else:
                print("ACCOUNT NUMBER IS INVALID")
                    
def wthdrw():
     b=0
     m=0  
     print("\n*************************************") 
     print("\n WITHDRAW ")
     print("\n*************************************") 
     print("\nEnter your Account Number")
     for b in range(b<i):
         if s[b].no == no: 
             m = b 
             if s[m].no == no: 
                 print(" Account Number : %d",s[m].no) 
                 print(" Name : %s",s[m].name)
                 print(" Deposit : %f",s[m].dep) 
                 print(" How Much Withdraw Now:") 
                 if s[m].dep<aa+500 :
                     print("CANNOT WITHDRAW YOUR ACCOUNT HAS MINIMUM BALANCE") 
                 else: 
                     s[m].dep-=aa 
                     print("The Balance Amount is:%f",s[m].dep) 
             else: 
                 print("INVALID")
                                              
def bal():
    b=0
    m=0 
    print("*************************************")              printf("\n BALANCE ENQUIRY "); 
    print("Enter your Account Number") 
    for b in range(b<i):        
        if(s[b].no == no): 
            m = b
            if(s[m].no==no):
                print(" Account Number : %d",s[m].no) 
                print(" Name : %s",s[m].name)
                print(" Deposit : %f",s[m].dep) 
                else:
                    print("INVALID")
                    
a=0
i = 101 
while True:
    print("\n*********************") 
    print("\n BANKING ") 
    print("\n*********************") 
    print("\n1-Creation") 
    print("\n2-Deposit") 
    print("\n3-Withdraw")
    print("\n4-Balance Enquiry") 
    print("\n5-Exit") 
    ch=int(input("\nEnter your choice"))                                                     printf("\n1-Creation"); 
    if ch==1:
        creatn()
    elif ch==2:
        depst()
    elif ch==3:
        wthdrw()
    elif ch==4:
        bal()
    elif ch==5:
        break    
              void deposit() 
         { 
                    int no,b=0,m=0; 
                    float aa; 
                    printf("\n*************************************"); 
                    printf("\n DEPOSIT "); 
                    printf("\n*************************************"); 
                    printf("\nEnter your Account Number"); 
                    scanf("%d",&no); 
                    for(b=0;b<i;b++) 
                        { 
                            if(s[b].no == no) 
                                m = b; 
                        } 
                            if(s[m].no == no) 
                              { 
                                         printf("\n Account Number : %d",s[m].no); 
                                         printf("\n Name : %s",s[m].name); 
                                         printf("\n Deposit : %f",s[m].dep); 
                                         printf("\n How Much Deposited Now:"); 
                                         scanf("%f",&aa); 
                                         s[m].dep+=aa; 
                                         printf("\nDeposit Amount is :%f",s[m].dep); 
                                         getch(); 
                              } 
                             else 
                              { 
                                        printf("\nACCOUNT NUMBER IS INVALID"); 
                                        getch(); 
                               } 
          } 
              void withdraw() 
          { 
                     int no,b=0,m=0; 
                     float aa; 
                     printf("\n*************************************"); 
                     printf("\n WITHDRAW "); 
                     printf("\n*************************************"); 
                     printf("\nEnter your Account Number"); 
                     scanf("%d",&no); 
                     for(b=0;b<i;b++) 
                         { 
                                if(s[b].no == no) 
                                  m = b; 
                         } 
                               if(s[m].no == no) 
                                  { 
                                         printf("\n Account Number : %d",s[m].no); 
                                         printf("\n Name : %s",s[m].name); 
                                         printf("\n Deposit : %f",s[m].dep); 
                                         printf("\n How Much Withdraw Now:"); 
                                         scanf("%f",&aa); 
                                         if(s[m].dep<aa+500) 
                                            { 
                                                   printf("\nCANNOT WITHDRAW YOUR ACCOUNT HAS MINIMUM BALANCE"); 
                                                   getch(); 
                                            } 
                                           else 
                                            { 
                                                   s[m].dep-=aa; 
                                                   printf("\nThe Balance Amount is:%f",s[m].dep); 
                                             } 
                                  } 
                                else 
                                 { 
                                       printf("INVALID"); 
                                       getch(); 
                                 } 
                                       getch(); 
           } 
                 void bal() 
           { 
                   int no,b=0,m=0; 
                   float aa; 
                   printf("\n*************************************"); 
                   printf("\n BALANCE ENQUIRY "); 
                   printf("\n*************************************"); 
                   printf("\nEnter your Account Number"); 
                   scanf("%d",&no); 
                   for(b=0;b<i;b++)        
                       { 
                            if(s[b].no == no) 
                              m = b; 
                       } 
                            if(s[m].no==no) 
                               { 
                                     printf("\n Account Number : %d",s[m].no); 
                                     printf("\n Name : %s",s[m].name); 
                                     printf("\n Deposit : %f",s[m].dep); 
                                     getch(); 
                               } 
                              else 
                              { 
                                     printf("INVALID"); 
                                     getch(); 
                               } 
             } 
 
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

class Account:
    def __init__(self, number, owner, balance):
        self.number = number
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction(amount, 'Deposit'))

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(Transaction(amount, 'Withdrawal'))
        else:
            print('Insufficient funds')

class Transaction:
    def __init__(self, amount, type):
        self.amount = amount
        self.type = type

def main():
    bank_name = input('Enter bank name: ')
    bank = Bank(bank_name)
    print('Bank', bank_name, 'created successfully')
    while True:
        print('1. Create Account')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            acc_number = input('Enter account number: ')
            acc_owner = input('Enter account owner name: ')
            acc_balance = float(input('Enter opening balance: '))
            account = Account(acc_number, acc_owner, acc_balance)
            bank.add_account(account)
            print('Account created successfully')
        elif choice == 2:
            acc_number = input('Enter account number: ')
            amount = float(input('Enter amount to deposit: '))
            account = find_account(bank.accounts, acc_number)
            if account:
                account.deposit(amount)
                print('Deposit successful')
            else:
                print('Account not found')
        elif choice == 3:
            acc_number = input('Enter account number: ')
            amount = float(input('Enter amount to withdraw: '))
            account = find_account(bank.accounts, acc_number)
            if account:
                account.withdraw(amount)
                print('Withdrawal successful')
            else:
                print('Account not found')
        elif choice == 4:
            print('Thank you for using the Bank Management System')
            break
        else:
            print('Invalid choice')

def find_account(accounts, number):
    for account in accounts:
        if account.number == number:
            return account
    return None

if __name__ == '__main__':
    main()

#def wait_lst():
'''    
lst=[]
avl_seat=5
wait_seat=3
while True:
    print("1.Booking 2.View 3.Cancel 4.Exit")
    ch=int(input("Enter Choice"))
    if ch==1:
        usrnm=input("Enter the Name")
        age=int(input("Enter the age"))
        src=input("Enter the Source")
        dest=input("Enter the Destination")
        num_seats=int(input("Enter number of seats"))
        if num_seats<avl_seat:
            print('.......Booked Successfully.......')
        else:
            wait_lst()
            break
    elif ch==2:
        print("---------------------------------------------")
        print('--------------------Details------------------')
        print("---------------------------------------------")
        print("Name\tAge\tSource\tDestination")
        print('%s\t%.2d\t%s\t%s'%(usrnm,age,src,dest))
        print("---------------------------------------------")
        
    elif ch==3:
        
        cncl_seat=int(input("Enter number of seats to cancel"))
        avl_seat=avl_seat-cncl_seat
        print("%d Seats is cancelled!"%avl_seat)

    elif ch==4:
        print('...............THANK MYSELF....................')
        break
    


try:
    print("Raising an error")
    raise ValueError
finally:
    print("In Finally Block")


n=int(input("Enter Number:"))
if n<0:
    raise Exception("Negative number not allowed")


try:
    n=int(input("Enter Numerator:"))
    d=int(input("Enter Denominator:"))
    q=n/d
    print("Quotient:",q)
except ZeroDivisionError:
    print("Denominator can not be Zero")
except ValueError:
    print("Invalid data type")
else:
    print("Successfully Terminating")


try:
    n=int(input("Enter Numerator:"))
    d=int(input("Enter Denominator:"))
    q=n/d
    print("Quotient:",q)
except ZeroDivisionError:
    print("Denominator can not be Zero")
except ValueError:
    print("Invalid data type")
except:
    print("Unknown Error")

try:
    n=int(input("Enter Numerator:"))
    d=int(input("Enter Denominator:"))
    q=n/d
    print("Quotient:",q)
except(ZeroDivisionError,ValueError):
    print("Denominator can not be Zero or Invalid data type")

try:
    n=int(input("Enter Numerator:"))
    d=int(input("Enter Denominator:"))
    q=n/d
    print("Quotient:",q)
except ZeroDivisionError:
    print("Denominator can not be Zero")
except ValueError:
    print("Invalid data type")

n=int(input("Enter Numerator:"))
d=int(input("Enter Denominator:"))
q=n/d
print("Quotient:",q)

n=int(input("Enter Numerator:"))
d=int(input("Enter Denominator:"))
try:
    q=n/d
    print("Quotient:",q)
except ZeroDivisionError:
    print("Denominator can not be Zero")


import time
def trffc_sgl():
    print("Red Light-Stop!")
    time.sleep(10)
    print("Yellow Light-Prepare to Stop!")
    time.sleep(5)
    print("Green Light-Go!")
    time.sleep(15)
for _ in range(3):
    trffc_sgl()
    
from math import pi,e
print(pi,'----',e)

import math
print(math.pi)

def nm():
    print("Name:----")
def rno():
    print("Roll No. :----")
print(__name__)
nm()
rno()

def depst():

    
    amt=int(input("Enter Deposit amount: "))
            avl_bal=avl_bal+amt
            t_id=random.randint(100000,999999)
            trnsctn=trnsctn+((t_id,accnt,ty,amt,avl_bal),)
            print("Deposit Done")
def whdrw():
    amt=int(input("Enter Withdraw amount:"))
    if amt<avl_bal:
        avl_bal=avl_bal-amt
        t_id=random.randint(100000,999999)
        trnsctn=trnsctn+((t_id,accnt,ty,amt,avl_bal),)
        print("Withdraw Done")
    else:
        print("Insufficiant Balance....Try again")


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




from functools import reduce
def add(x,y):
    return x+y
num=[1,2,3,4,5]
res=reduce(add,num)
print(res)

def sqr(x):
    return x**2
num=[1,2,3,4,5]
sqr_lst=map(sqr,num)
print(list(sqr_lst))

def evn_chck(n):
    return n%2==0
num=range(21,30)
evn_lst=list(filter(evn_chck,num))
print(evn_lst)

def fact(num):
    if num==1:
       return(num)
    else:
       return(num*fact(num-1))

n=int(input("enter a positive number"))
print(fact(n))
#res=fact(n)
#print(res)

def gcd_rcursve(n1,n2)
    if n2==0:
        return n1
    else:
        return gcd_rcursve(n2,n1%n2)
num1=48
num2=18
result=gcd_rcursve(num1,num2)    
print(f"The GCD of {num1} and {num2} is:{result}")

def outer_fun():
    def inner_fun():
        print("Welcome to Python")
    inner_fun()
outer_fun()
'''
