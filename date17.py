'''
Q=[]
size=int(input('enter size'))
def enq():
    if len(Q)==size:
        print('Overflow')
    else:
        ele=int(input('Enter element:'))
        Q.append(ele)
def deq():
    if len(Q)==0:
        print('Underflow')
    else:
        print(Q.pop(0),'deleted')
def peek():
    if len(Q)==0:
        print('Queue is Empty')
    else:
        print(Q[0],'first element')

while True:
    print('1.Insert 2.Delete 3.Peek 4.Exit')
    ch=int(input('Enter choice'))
    if ch==1:
        enq()
    elif ch==2:
        deq()
    elif ch==3:
        peek()
    elif ch==4:
        break

    
strg=input("enter the string")
print(len(strg))

size=int(input('Enter the size'))
class Node:
    def __init__(self,ele):
        self.data=ele
        self.next=None
        print('Node created')
class Stack:
    def __init__(self):
        self.top=None
    def push(self,ele):
        nn=Node(ele)
        if self.top is None:
            self.top=nn
        else:
            nn.next=self.top
            self.top=nn
    def pop_ele(self):
        if self.top is None:
            print('underflow')
        else:
            print(self.top.data,'poped')
            self.top=self.top.next
    def pop(self):
        if self.top is None:
            print('underflow')
        else:
            current=self.top
            self.top=current.next
            print(current.data,'poped')
            del current
    def peek(self):
        if self.top is None:
            print('Stack is Empty')
        else:
            print('Top Element:',self.top.data)
stk=Stack()
while True:
    print('4.pop_ele 1.push 2.pop 3.display 5.exit')
    ch=int(input('Enter choice'))
    if ch==1:
        ele=int(input('Enter element to push'))
        stk.push(ele)
    elif ch==2:
        stk.pop()
    elif ch==3:
        stk.peek()
    elif ch==4:
        stk.pop_ele
    elif ch==5:
        break


stack=[]
size=int(input('Enter the size of stack'))
def push_ele():
    if size==len(stack):
        print('overflow')
    else:
        ele=int(input('Enter the element to push'))
        stack.append(ele)
        print(ele,'Element pushed successfully')
def pop_ele():
    if len(stack)==0:
        print('underflow')
    else:
        print(stack.pop(),'Poped from stack')
def peek_ele():
    if len(stack)==0:
        print('underflow')
    else:
        print(stack[-1],'is top of the stack')
while True:
    print('1.push 2.pop 3.display 4.exit')
    ch=int(input('Enter choice'))
    if ch==1:
        push_ele()
    elif ch==2:
        pop_ele()
    elif ch==3:
        peek_ele()
    elif ch==4:
        break


inp=input('Enter the number is the form of string')
inger=int(inp)
print(inger**2)
'''

