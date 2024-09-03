# Queue using single linked list--

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self, head=None):
        self.head = head

    def enqueue(self,data):
        newnode=Node(data)
        newnode.item=data
        if self.head==None:
            newnode.next=None
            self.head=newnode
        else:
            newnode.next=None
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=newnode
        
    def dequeue(self):
        if self.head==None:
            print("\nNo node avaliable to delete!!")
            return
        else:
            if self.head.next==None:
                self.head=None
            else:
                self.head=self.head.next

    def front(self):
        if self.head==None:
            print("\nNo front value!!")
            return
        else:
            print(self.head.item)
            return
    
    def rear(self):
        if self.head==None:
            print("\nNo rear value!!")
            return
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            print(temp.item)
    
    def search(self,data):
        temp=self.head
        if temp is None:
            print("\nNo node avaliable to search!!")
            return
        else:
            while temp.next is not None:
                if temp.item==data:
                    print("\nSearch Succesfull..")
                    return
                temp=temp.next
            while temp.item ==data:
                print("\nSearch Succesfull..")
                return
            else:
                print("\nSearch Un-Succsfull")
            
    def count(self):
        Count=0
        temp=self.head
        while temp is not None:
            Count+=1
            temp=temp.next
        print("\n",Count)

    def print_data(self):
        if self.head is None:
            print("\nNo data available to Print!!")
            return
        else:
            temp = self.head
            print("\n")
            while temp.next is not None:
                print(temp.item, end=" ")
                temp = temp.next
            print(temp.item)

myqueue=Queue()
while True:
    print("\n1. enqueue an element")
    print("2. dequeue an element")
    print("3. Front element print")
    print("4. Rear element print")
    print("5. Search an element")
    print("6. Print the Queue")
    print("7. Exit")
    
    choice=int(input("\nEnter your choice: "))
    
    if choice==1:
        data=int(input("Enter the data to insert: "))
        myqueue.enqueue(data)
    elif choice==2:
        myqueue.dequeue()
    elif choice==3:
        myqueue.front()
    elif choice==4:
        myqueue.rear()
    elif choice==5:
        data=int(input("Enter data to search: "))
        myqueue.search(data)
    elif choice==6:
        myqueue.print_data()
    elif choice==7:
        break
    else:
        print("Wrong choice!!")