'''for i in range(0,128):
    print(chr(i),"%d \t"%i,end=' ')
'''
'''s=input()
for i in s:
    print(i,"%d \t"%ord(i),end=' ')
'''
'''s=input()
fc=s[0]
for i in range(len(s)):
    if s[i]==fc.upper() or s[i]==fc.lower():
        s=s[:i]+'$'+s[i+1:]
r=fc+s[1:]
print(s)
print(r)
'''
'''s=input()
if len(s)<=3:
    print(s)
elif  s.endswith('ing'):
    print(s+'ly')
else:
    print(s+'ing')
  '''  
'''s=input()
if len(s)<=3:
    print(s)
elif  s.endswith('ing'):
    print(s.
          replace('ing','ly'))
else:
    print(s+'ing')
 '''
s=input()
if len(s)>8:
    print(len(s))
    



























'''user_name1=input("enter the 1st user name")
card1=int(input("enter 1st card number"))
pin1=int(input("enter 1st card pin"))
pin_no=123456
user_name2=input("enter the 2nd user name")
card2=int(input("enter 2nd card number"))
pin2=int(input("enter 2nd card pin"))
ch1="details"
ch2="forgot"
wt=input("req")
if ch1==wt:
    c=int(input("enter card number"))
    if card1==c1:
        print(f"The user detials are:\n user name :{user_name1}  user card no.:{card1}")
    elif card2==c:
        print(f"The user detials are:\n user name :{user_name2}  user card no.:{card2}")
elif ch2==wt:
    c=int(input("enter card number"))
    if c==card1:
        upin=int(input("enter new pin"))
        cnpin=int(input("confirm pin"))
        if upin==cnpin:
            pin1=upin
            print("updated successfully",pin1)
        else:
            wt=input("req")
            
    elif c==card2:


        upin=int(input("enter new pin"))
        cnpin=int(input("confirm pin"))
        if upin==cnpin:
            pin2=upin
            print("updated successfully",pin2)
        else:
            wt=input("req")
    else:
        print("wrong card number")


'''
'''elif wt=="username"'''
    






            
'''if pin1==pin_no:
    print(f"The user detials are:{user_name} {card1}")
elif pin2==pin_no:
    print(f"the card detials is:{user_name} {card2}")
else:
    if usr_inp=="yes":
        n=int(input("enter card number"))
        if n==card1:
            pin1=int(input("enter new pin of card 1"))
        elif n==card2:
            pin2=int(input("enter new pin of card 2"))
    

'''

'''elif user_input==fgt_pwd:
    card_dt=int(input("enter the card number to recreate the pin"))
    if int(user_input)==card1:
        pin1=int(input("enter new password for 1st card"))
    elif int(user_input)==card2:
        pin2=int(input("enter new password for 1st card"))
else:
    user_input=input("enter qurries")

if int(user_input)==card1:
    print(f"The card1 details after udating are: card no.:{card1} pin:{pin1}")
elif int(user_input)==card2:
     print(f"The card2 details after udating are: card no.:{card2} pin:{pin2}")
     
op1=input("    
'''    







            
