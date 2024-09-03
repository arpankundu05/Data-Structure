# Code for Circularlinkedlist..

# Create a node class for create node-
class Node:
	def __init__(self, item=None,next=None):
		self.item = item
		self.next = next

# Create Circular link list-
class Circular_Linked_List:
    def __init__(self, last=None):
        self.last = last

    # insert a data in start-
    def insert_at_start(self, data):
        newnode = Node(data)
        # self.data=data
        if self.last==None:
            self.last=newnode
            newnode.next=newnode
        else:
            newnode.next=self.last.next
            self.last.next=newnode
    
    # Insert a data in last-
    def insert_at_last(self,data):
        newnode=Node(data)
        if self.last==None:
            self.last=newnode
            newnode.next=newnode
        else:
            newnode.next=self.last.next
            self.last.next=newnode
            self.last=newnode
            
    # Insert a data in any position-
    def insert_any_position(self,pos,data):
        if pos<0:
            print("\nInvalid")
            return
        elif pos==0:
            self.insert_at_start(data)
            return
        else:
            temp=self.last.next
            newnode=Node(data)
            for i in range(pos-1):
                temp=temp.next
                if temp==self.last:
                    print("\nPosition out of range")
                    return
            newnode.next=temp.next
            temp.next=newnode
            if newnode.next==self.last:
                self.last=newnode
                
    # Delete the first node-
    def delete_at_start(self):
        if self.last==None:
            print("\nNothing to be deleted")
            return
        else:
            if self.last.next==self.last:
                self.last=None
            else:
                self.last.next=self.last.next.next
    
    # Delete the last node
    def delete_at_last(self):
        if self.last==None:
            print("\nNothing to be deleted")
            return
        else:
            if self.last.next==self.last:
                self.last==None
            else:
                temp=self.last.next
                while temp.next!=self.last:
                    temp=temp.next
                temp.next=self.last.next
                self.last=temp
    
    # delete any  position of the node  
    def delete_any_position(self, pos):
        if pos < 0:
            print("\nInvalid position")
            return
        elif pos == 0:
            self.delete_at_start()
            return
        else:
            temp = self.last.next
            prev = None
            for i in range(pos):
                prev = temp
                temp = temp.next
                if temp == self.last.next:
                    print("\nPosition out of range")
                    return
            if temp == self.last:
                prev.next = temp.next
                self.last = prev
            else:
                prev.next = temp.next

    # Search any element of the list-
    def search(self,data):
        if self.last==None:
            print("\nSearch Un-succsfull!!")
            return
        else:
            temp=self.last.next
            while temp !=self.last:
                if temp.item==data:
                    print("\nSearch Succsfull..")
                    return
                temp=temp.next
            if temp.item==data:
                print("\nSearch Succsfull..")
            else:
                print("\nSearch Un-succsfull!!")

    # print the list--
    def print_list(self):
        if self.last==None:
            print("\nNothing to be printed!!")
            return
        else:
            temp=self.last.next
            while temp!=self.last:
                print(temp.item,end=" ")
                temp=temp.next
            print(temp.item)

# Driver code-
CLL=Circular_Linked_List()
while True:
    print("\n1. Insert at start")
    print("2. Insert at end")
    print("3. Insert at any position")
    print("4. Delete first")
    print("5. Delete last")
    print("6. Delete at any position")
    print("7. Search")
    print("8. Print list")
    print("9. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        data = int(input("Enter data to insert at start: "))
        CLL.insert_at_start(data)
    elif choice == 2:
        data = int(input("Enter data to insert at end: "))
        CLL.insert_at_last(data)
    elif choice == 3:
        pos = int(input("Enter position to insert: "))
        data = int(input("Enter data to insert: "))
        CLL.insert_any_position(pos, data)
    elif choice == 4:
        CLL.delete_at_start()
    elif choice == 5:
        CLL.delete_at_last()
    elif choice == 6:
        position = int(input("Enter position to delete: "))
        CLL.delete_any_position(position)
    elif choice == 7:
        data = int(input("Enter data to search: "))
        CLL.search(data)
    elif choice == 8:
        print("\n")
        CLL.print_list()
    elif choice == 9:
        break
    else:
        print("Invalid choice. Please try again.")