class Node:
    def __init__(self,ele):
        self.prev=None
        self.data=ele
        self.next=None
class DoubleLinkedList:
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
            nn.prev=current
    def display(self):
        if self.head==None:
            print('List is Empty')
        else:
            current=self.head
            while current:
                print(current.data)
                current=current.next
    def rev_dsply(self):
        if self.head==None:
            print('List is Empty')
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            while current:
                print(current.data)
                current=current.prev
    def insert_begin(self,ele):
        nn=Node(ele)
        if self.head==None:
            self.head=nn
        else:
            current=self.head
            nn.next=current.prev
            current.next=None
        self.head=nn
        '''current.prev=nn.next
            nn.prev=None
            nn.next=current
             nn.next=self.head
            self.head=nn
            '''
dll=DoubleLinkedList()
while True:
    print('1.Insert@last 2.Insert@Begin  3.Display 4.Reverse_Display 5.Exit')
    ch=int(input('Enter choice:'))
    if ch==1:
        ele=int(input('Enter the element: '))
        dll.insert_last(ele)
    elif ch==2:
        ele=int(input('Enter the element: '))
        dll.insert_begin(ele)
    elif ch==3:
        dll.display()
    elif ch==4:
        dll.rev_dsply()
    elif ch==5:
        break
'''
class Node:
    def __init__(self,ele):
        self.prev=None
        self.data=ele
        self.next=None
n1=Node(100)
n2=Node(150)
n3=Node(200)
n1.next=n2
n2.prev=n1
n2.next=n3
n3.prev=n2
start=n1

while start:
    print(start.data)
    start=start.next

print()

start=n3

while start:
    print(start.data)
    start=start.prev


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
    
    def insert_begin_SLL(self,target,element):
        nn=Node(element)
        
        if self.head is None:
            print("list is empty")
            
        elif self.head.data==target:
            nn.next=self.head
            self.head=nn
            
        elif self.head.next.data==target:
            nn.next=self.head.next
            self.head.next=nn
        else:
            current=self.head
            while current.next and current.next.data!=target:
                current=current.next
            if  current.next:
                nn.next=current.next
                current.next=nn
            else:
                print("Data not found")
    def insert_last_SLL(self,target,element):
        nn=Node(element)
        
        if self.head is None:
            print("list is empty")
            
        elif self.head.data==target:
            self.head.next=nn
            self.head==nn

        elif self.head.next.data==target:
            curr=self.head
            curr.next.next=nn
        else:
            current=self.head
            while current.next!=None:
                prev=current
                current=current.next
            if current:
                current.next=nn
            else:
                print('not found')
    def insertAfterNode(self,target,element):
        nn=Node(element)
        current=self.head
        while current and current.data!=target:
            current=current.next
        if current:
            nn.next=current.next
            current.next=nn
        else:
            print("Node with data",target,'not found')
    def display(self):
        if self.head==None:
            print('List is empty')
        else:
            current=self.head
            while current:
                print(current.data,end=' ')
                current=current.next
            print()

    def reverse(self):
        current=self.head
        prev=None
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head=prev
llst=LinkedList()
while True:
    print('...........................................................')
    print(' 0.insertafternode\n 1. SLL Insert@Begin\n 2. SLL Insert@Last\n 3.Insert@Begin\n 4.Insert@End\n 5.Display\n 6.Reverse\n 7.Exit')
    print('...........................................................')
    ch=int(input('Enter choice '))
    if ch==0:
        ele=int(input('Enter the element '))
        tar=int(input('Enter the target '))
        llst.insertAfterNode(tar,ele)
    if ch==1:
        ele=int(input('Enter the element '))
        tar=int(input('Enter the target '))
        llst.insert_begin_SLL(tar,ele)
        print('Node inserted at beginning successfully')
    elif ch==2:
        ele=int(input('Enter the element '))
        tar=int(input('Enter the target '))
        llst.insert_last_SLL(tar,ele)
        print('Node inserted at ending successfully')
    elif ch==3:
        ele=int(input('Enter element to insert'))
        llst.insert_begin(ele)
        print('Node Inserted at beginning Successfully')
    elif ch==4:
        ele=int(input('Enter element to insert'))
        llst.insert_last(ele)
        print('Node Inserted at ending Successfully')
    elif ch==5:
        llst.display()

    elif ch==6:
        llst.reverse()
    elif ch==7:
        break








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
        print('Node Inserted at ending Successfully')
    elif ch==2:
        ele=int(input('Enter element to insert'))
        llst.insert_begin(ele)
        print('Node Inserted at beginning Successfully')
    elif ch==3:
        llst.del_begin()
    elif ch==4:
        llst.del_last()
    elif ch==5:
        llst.display()
    elif ch==6:
        break
'''

