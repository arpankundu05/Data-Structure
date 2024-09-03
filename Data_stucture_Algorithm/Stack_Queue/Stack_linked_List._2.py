# Stack using single linked list without travarsing--

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self, head=None):
        self.head = head
        self.Count=0

    def push(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
        self.Count+=1
    
    def pop(self):
        self.head=self.head.next
        self.Count-=1
    
    def peek(self):
        if self.head == None:
            print("Nothing peek value!!")
            return
        else:
            print(self.head.item)
            
    def count(self):
        print(self.Count)
    
    def print_data_reverse(self, node=None):
        if node is None:
            node = self.head
        if node is None:
            return
        self.print_data_reverse(node.next)
        print(node.item, end=" ")
            
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
        mystack.print_data_reverse()
    elif choice==6:
        mystack.count()
    elif choice==7:
        break
    else:
        print("Wrong choice!!")