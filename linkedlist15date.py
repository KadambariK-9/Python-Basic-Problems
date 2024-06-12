class Node:
    def __init__(self,ele):
        self.data=ele
        self.next=None
        print('Node Created')
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_last(self,ele):
        nn=Node(ele)
        if self.head==None:
            self.head=nn
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=nn
    def insert_begin(self,ele):
        nn=Node(ele)
        if self.head==None:
            self.head=nn
        else:
            nn.next=self.head
            self.head=nn
            print("node inserted")
    def del_begin(self):
        if self.head==None:
            print('List is empty,not possible to delete')
        else:
            current=self.head
            self.head=current.next
            print(current.data,'deleted')
            del current
    def del_last(self):
        if self.head==None:
            print('List is empty,not possible to delete')
        else:
            current=self.head
            while current.next!=None:
                prev=current
                current=current.next
            print(current.data,'deleted')   
            prev.next=None
            del current
    def search(self):      
    def display(self):
        if self.head==None:
            print('List is empty')
        else:
            current=self.head
            while current:
                print(current.data,end=' ')
                current=current.next
            print()
llst=LinkedList()
while True:
    print('1. Insert@End  2.Insert@Begin 3.Delete@Begin 4.Delete@End 5.Display  6.Exit')
    ch=int(input('Enter Your Choice'))
    if ch==1:
        ele=int(input('Enter element to insert'))
        llst.insert_last(ele)
        print('Node Inserted Successfully')
    elif ch==2:
        ele=int(input('Enter element to insert'))
        llst.insert_begin(ele)
        print('Node Inserted Successfully')
    elif ch==3:
        llst.del_begin()
    elif ch==4:
        llst.del_last()
    elif ch==5:
        llst.display()
    elif ch==6:
        break


'''class Node:
    def __init__(self,ele):
        self.data=ele
        self.next=None
        print('Node Created')
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,ele):
        nn=Node(ele)
        if self.head==None:
            self.head=nn
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=nn
    def display(self):
        if self.head==None:
            print('List is empty')
        else:
            current=self.head
            while current:
                print(current.data,end=' ')
                current=current.next
            print()
llst=LinkedList()
while True:
    print('1. Insert 2.Display 3.Exit')
    ch=int(input('Enter Your Choice'))
    if ch==1:
        ele=int(input('Enter element to insert'))
        llst.insert(ele)
        print('Node Inserted Successfully')
    elif ch==2:
        llst.display()
    elif ch==3:
        break




class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
    def display(self):
        while self:
            print(self.data,end=' ')
            self=self.next
n1=Node(100)
n2=Node(150)
n1.next=n2
n3=Node(200)
n2.next=n3
n1.display()


class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
n1=Node(100)
n2=Node(150)
n3=Node(200)
n1.next=n2
n2.next=n3
start=n1
while start:
    print(start.data)
    start=start.next
'''
