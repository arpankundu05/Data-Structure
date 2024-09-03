# Stack using single linked list-

# Create The node
class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self, head=None):
        self.head = head

    def push(self, data):
        newnode = Node(data)
        if self.head is None:
            newnode.next = None
            self.head = newnode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newnode
            
    def pop(self):
        if self.head==None:
            print("\nNo node avaliable to delete!!")
            return
        elif self.head.next==None:
                self.head=None
        else:
            temp=self.head
            while temp.next.next != None:
                temp=temp.next
            temp.next=None
    
    def peek(self):
        temp=self.head
        if temp is None:
            print("\nNo peek value")
            return
        else:
            while temp.next is not None:
                temp=temp.next
            print("\n",temp.item)
    
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

mystack=Stack()
while True:
    print("\n1. Push an element")
    print("2. Pop an element")
    print("3. Peek an element")
    print("4. Search an element")
    print("5. Print the stack")
    print("6. Count data")
    print("7. Exit")
    
    choice=int(input("\nEnter your choice: "))
    
    if choice==1:
        data=int(input("Enter the data to insert: "))
        mystack.push(data)
    elif choice==2:
        mystack.pop()
    elif choice==3:
        mystack.peek()
    elif choice==4:
        data=int(input("Enter data to search: "))
        mystack.search(data)
    elif choice==5:
        mystack.print_data()
    elif choice==6:
        mystack.count()
    elif choice==7:
        break
    else:
        print("Wrong choice!!")