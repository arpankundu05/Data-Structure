class Node:
	def __init__(self,item=None,next=None):
		self.item=item
		self.next=next

class Piority_queue:
    def __init__(self,head=None):
        self.head=head
        
    # Push an element
    def push(self, data):
        newnode = Node(data)
        if self.head is None or self.head.item >= data:
            newnode.next = self.head
            self.head = newnode
        else:
            temp = self.head
            while temp.next is not None and temp.next.item < data:
                temp = temp.next
            newnode.next = temp.next
            temp.next = newnode
            
    # Delete an element
    def pop(self):
        if self.head==None:
            print("No node avaliable to delet!!")
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

    # To print peek value
    def peek(self):
        if self.head==None:
            print("No peek value!!")
            return
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            print(temp.item)

    # Search for an element
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
            print("\nSearch Failed!!")

    # Print the data
    def print_data(self):
        temp=self.head
        if temp is None:
            print("Nothing to be printed!!")
            return
        else:
            while temp is not None:
                print(temp.item,end=" ")
                temp=temp.next
        print("\n")
        
myqueue=Piority_queue()
while True:
    print("\n1. Push an element")
    print("2. Pop an element")
    print("3. Peek an element")
    print("4. Search an element")
    print("5. Print the piority queue")
    print("6. Exit")
    
    choice=int(input("\nEnter your choice: "))
    
    if choice==1:
        data=int(input("Enter the data to insert: "))
        myqueue.push(data)
    elif choice==2:
        myqueue.pop()
    elif choice==3:
        myqueue.peek()
    elif choice==4:
        data=int(input("Enter data to search: "))
        myqueue.search(data)
    elif choice==5:
        myqueue.print_data()
    elif choice==6:
        break
    else:
        print("Wrong choice!!")