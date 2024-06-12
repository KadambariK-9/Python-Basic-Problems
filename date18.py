class Node:
    def __init__(self,val,prity):
        self.data=val
        self.priority=prity
        self.next=None
class PriorityQueue:
    def __init__(self):
        self.front=None
    def is_empty(self):
        return self.front is None
    def enqueue(self,data,priority):
        nn=Node(data,priority)
        if self.is_empty() or priority>self.front.priority:
            nn.next=self.front
            self.front=nn
        else:
            current=self.front
            while current.next and current.next.priority>priority:
                current=current.next
            nn.next=current.next
            current.next=nn
    def dequeue(self):
        if self.is_empty():
            print('Queue is Underflow')
            return None
        data=self.front.data
        self.front=self.front.next
        return data
    def peek(self):
        if self.is_empty():
            print('Queue is Empty')
        else:
            print('Peek of element:',self.front.data)
    def display(self):
        if self.is_empty():
            print('Queue is Empty')
        else:
            current=self.front
            while current:
                print(f"({current.data},{current.priority})",end=' ')
                current=current.next
            print()
pq=PriorityQueue()
while True:
    print('1.EnQueue 2.DeQueue 3.Display 4.Peek 5.Exit')
    ch=int(input('Enter Choice'))
    if ch==1:
        ele=int(input("Enter element"))
        prity=int(input("Enter priority"))
        pq.enqueue(ele,prity)
    elif ch==2:
        pq.dequeue()
    elif ch==3:
        pq.display()
    elif ch==4:
        pq.peek()
    elif ch==5:
        print('Terminated Successfully')
        break

            
'''
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class CircularQueue:
    def __init__(self,size):
        self.front=None
        self.rear=None
        self.size=size
        self.count=0
    def is_full(self):
        return self.count==self.size
    def is_empty(self):
        return self.count==0
    def enqueue(self,data):
        if self.is_full():
            print('Queue is Overflow')
            return
        nn=Node(data)
        if self.is_empty():
            self.front=nn
        else:
            self.rear.next=nn
        self.rear=nn
        self.rear.next=self.front
        self.count+=1
    def dequeue(self):
        if self.is_empty():
            print('Queue is Underflow')
        else:
            data=self.front.data
            if self.front==self.rear:
                self.front=None
                self.rear=None
            else:
                self.front=self.front.next
                self.rear.next=self.front
            self.count-=1
            print(data,'deleted')
    def peek(self):
        if self.is_empty():
            print('Queue is empty')
        else:
            print('Peek of a element:',self.front.data)
    def dsply(self):
        if self.is_empty():
            print('Queue is empty')
        else:
            temp=self.front
            while True:
                print(temp.data,end=' ')
                temp=temp.next
                if temp==self.front:
                    break
            print()
size=int(input("Enter Size:"))
q=CircularQueue(size)
while True:
    print('1.EnQueue 2.DeQueue 3.Display 4.Peek 5.Exit')
    ch=int(input('Enter Choice'))
    if ch==1:
        data=int(input("Enter element"))
        q.enqueue(data)
    elif ch==2:
        q.dequeue()
    elif ch==3:
        q.dsply()
    elif ch==4:
        q.peek()
    elif ch==5:
        print('Terminated Successfully')
        break
    else:
        print('Invalid choice , Please Try Again')







class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class Queue:
    def __init__(self):
        self.front=self.rear=None
    def enq(self):
        ele=ele=int(input('Enter Element'))
        nn=Node(ele)
        if self.rear is None:
            self.front=self.rear=nn
        else:
            self.rear.next=nn
            self.rear=nn
    def deq(self):
        if self.front is None:
            print('Queue Underflow')
        else:
            ele=self.front.data
            self.front=self.front.next
            if self.front is None:
                self.rear=None
            print(ele,'deleted from queue')
    def dsply(self):
        if self.front is None:
            print('Queue Underflow')
        else:
            curr=self.front
            while curr:
                print(curr.data,end=' ')
                curr=curr.next
            print()
    def peek(self):
        if self.front is None:
            print('Queue Empty')
        else:
            print(self.front.data,end=' ')
            print()
q=Queue()
while True:
    print('1.EnQueue 2.DeQueue 3.Display 4.Peek 5.Exit')
    ch=int(input('Enter Choice'))
    if ch==1:
        q.enq()
    elif ch==2:
        q.deq()
    elif ch==3:
        q.dsply()
    elif ch==4:
        q.peek()
    elif ch==5:
        print('Terminated Successfully')
        break
    else:
        print('Invalid choice , Please Try Again')







que=[]
frnt=rr=-1
sz=int(input("Enter Size:"))
def en__que():
    if len(que)==sz:
        print('Queue Overflow')
    else:
        ele=int(input('Enter Element'))
        que.append(ele)
        print(que)
def de__que():
    if not que:
        print('Queue Underflow')
    else:
        ele=que.pop(0)
        print('Element dequeued from queue is',ele)
def display():
    if not que:
        print('Queue Underflow')
    else:
        print('Queue elements:',end=' ')
        for item in que:
            print(item,end=' ')
        print()
def en_que():
    global frnt,rr
    if rr==sz-1:
        print('Queue Overflow')
    else:
        ele=int(input('Enter Element'))
        if rr==-1:
            frnt=0
        rr=rr+1
        que.append(ele)
        print(que)
def de_que():
    global frnt,rr
    if frnt==-1 or frnt>rr:
        print('Queue Underflow')
    else:
        ele=que[frnt]
        frnt=frnt+1
        print('Element dequeued from queue is',ele)
def dsply():
    if frnt==-1 or frnt>rr:
        print('Queue is Empty')
    else:
        for i in range(frnt,rr+1):
            print(que[i],end=' ')
        print()
def peek():
    if frnt==-1 or frnt>rr:
        print('Queue is Empty')
    else:
        print('Front Element of the queue is',que[frnt])
while True:
    print('1.EnQueue 2.DeQueue 3.Display 4.Peek 5.Exit')
    ch=int(input('Enter Choice'))
    if ch==1:
        en_que()
    elif ch==2:
        de_que()
    elif ch==3:
        dsply()
    elif ch==4:
        peek()
    elif ch==5:
        print('Terminated Successfully')
    else:
        print('Invalid choice , Please Try Again')

'''











    



        
