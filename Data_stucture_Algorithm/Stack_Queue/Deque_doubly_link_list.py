# Deque using doubly linked list--

# Create The node--
class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class Deque:
    def __init__(self,head=None):
        self.head=head
        
    def insert_front(self,data):
        newnode = Node(None,data,self.head)
        self.data = data
        if self.head is None:
            self.head = newnode
        else:
            self.head.prev = newnode
            newnode.next = self.head
            self.head = newnode
    
    def insert_rear(self,data):
        newnode = Node()
        newnode.item = data
        newnode.next = None
        if self.head is None:
            newnode.prev = None
            self.head = newnode
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newnode
        newnode.prev = temp
    
    def delete_front(self):
        if self.head is None:
            print("\nDeque is empty!!")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None
    
    def delete_rear(self):
        if self.head is None:
            print("\nDeque is empty!!")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.prev.next = None
    
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
        if self.head is None:
            print("\nNo data avaliable to search")
            return
        temp = self.head
        while temp is not None:
            if temp.item == data:
                print("\nSearch Succesfull..")
                return
            temp = temp.next
        print("\nSearch Un-succesfull!!")
    
    def print_data(self):
        temp = self.head
        if temp is None:
            print("\nNothing to be printed!!")
            return
        else:
            while temp is not None:
                print(temp.item, end=" ")
                temp = temp.next
        print("\n")

mydeque=Deque()
while True:
    print("\n1. Insert an element at front")
    print("2. Insert an element at rear")
    print("3. Delete an element at front")
    print("4. Delete an element at rear")
    print("5. Front element print")
    print("6. Rear element print")
    print("7. Search an element")
    print("8. Print the Queue")
    print("9. Exit")
    
    choice=int(input("\nEnter your choice: "))
    
    if choice==1:
        data=int(input("Enter the data to insert: "))
        mydeque.insert_front(data)
    elif choice==2:
        data=int(input("Enter the data to insert: "))
        mydeque.insert_rear(data)
    elif choice==3:
        mydeque.delete_front()
    elif choice==4:
        mydeque.delete_rear()
    elif choice==5:
        mydeque.front()
    elif choice==6:
        mydeque.rear()
    elif choice==7:
        data=int(input("Enter data to search: "))
        mydeque.search(data)
    elif choice==8:
        mydeque.print_data()
    elif choice==9:
        break
    else:
        print("Wrong choice!!")