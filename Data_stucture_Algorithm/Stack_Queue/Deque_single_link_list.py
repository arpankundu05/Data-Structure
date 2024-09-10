# Deque using single linked list--

# Create The node
class Node:
	def __init__(self,item=None,next=None):
		self.item=item
		self.next=next

class Deque:
    def __init__(self,head=None):
        self.head=head

    # Insert an element at front
    def insert_front(self,data):
        newnode=Node(data)
        newnode.data=data
        if self.head==None:
            self.head=newnode
            newnode.next=None
        else:
            newnode.next=self.head
            self.head=newnode
            
    # Insert an element at rear
    def insert_rear(self,data):
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

    # Delete an element at front
    def delete_front(self):
        if self.head==None:
            print("\nNo data avaliable to delete!!")
            return
        else:
            if self.head.next==None:
                self.head=None
            else:
                self.head=self.head.next
    
    # Delete an element at rear
    def delete_rear(self):
        if self.head==None:
            print("\nNo data avaliable to delete!!")
            return
        else:
            if self.head.next==None:
                self.head=None
                return
            else:
                temp=self.head
                while temp.next.next != None:
                    temp=temp.next
                temp.next=None
                return

    # Check front value
    def front(self):
        if self.head==None:
            print("\nNo front value!!")
            return
        else:
            print(self.head.item)
            return
    
    # Check rear value
    def rear(self):
        if self.head==None:
            print("\nNo rear value!!")
            return
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            print(temp.item)
    
    # Search an element
    def search(self,data):
        if self.head==None:
            print("\nNo node avaliable!!")
            return
        temp=self.head
        while temp is not None:
            if temp.item==data:
                print("\nSearch Succesfull..")
                return
            temp=temp.next
        else:
            print("\nSearch Un-succesfull!!")
    
    # Print the deque
    def print_data(self):
        temp=self.head
        if temp is None:
            print("\nNothing to be printed!!")
            return
        else:
            while temp is not None:
                print(temp.item,end=" ")
                temp=temp.next
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