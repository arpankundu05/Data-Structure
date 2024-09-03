class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class Doubly_linked_list:
    def __init__(self, head=None):
        self.head = head

    # Insert an element at the first of the linked list
    def insert_at_first(self,data):
        newnode = Node(None,data)
        self.data = data
        if self.head is None:
            self.head = newnode
        else:
            self.head.prev = newnode
            newnode.next = self.head
            self.head = newnode
            
    # Insert an element at the end of the linked list
    def insert_at_last(self, data):
        newnode = Node()
        newnode.item = data
        newnode.next = None
        if self.head is None:
            newnode.prev = None
            self.head = newnode
            return
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newnode
            newnode.prev = temp

    # Insert an element at any position of the linked list
    def insert_any_pos(self, pos, data):
        newnode=Node(None,data)
        self.data=data
        if pos==0:
            self.insert_at_first(data)
        else:
            index=0
            temp=self.head
            while (index<pos-1 and temp.next is not None):
                index=index+1
                temp=temp.next
            newnode.next = temp.next
            newnode.prev = temp
            temp.next.prev = newnode
            temp.next = newnode
    
    # Delete first element from the list
    def delete_first(self):
        if self.head is None:
            print("\nNo node avaliable to delete!!")
            return
        else:
            self.head = self.head.next

    # Delete last element from the list
    def delete_last(self):
        if self.head is None:
            print("\nNo node avaliable to delete!!")
            return
        elif self.head.next is None:
            self.head = None
            return
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None
            
            
    # Delete element at any position
    def delete_any_pos(self, pos):
        if pos==0:
            self.delete_first()
        else:
            index=0
            temp=self.head
            while (index<pos-1 and temp.next is not None):
                index=index+1
                temp=temp.next
            next_node = temp.next.next
            temp.next = None
            temp.next = next_node
    
    # Search for an element
    def search(self, data):
        if self.head is None:
            print("\nNo data avaliable to search!!")
            return
        temp = self.head
        while temp is not None:
            if temp.item == data:
                print("\nSearch Succcesfull..")
                return
            temp = temp.next
        print("\nSearch Un-succesfull!!")
        
    # Print the list
    def print_list(self):
        temp = self.head
        if temp is None:
            print("Nothing to be printed!!")
            return
        else:
            while temp is not None:
                print(temp.item, end=" ")
                temp = temp.next
        print("\n")

DLL = Doubly_linked_list()
while True:
    print("\n1. Insert at start")
    print("2. Insert at end")
    print("3. Insert at any position")
    print("4. Delete first")
    print("5. Delete last")
    print("6. Delete at any position")
    print("7. Search")
    print("8. Print data")
    print("9. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        data = int(input("Enter data to insert at start: "))
        DLL.insert_at_first(data)
    elif choice == 2:
        data = int(input("Enter data to insert at end: "))
        DLL.insert_at_last(data)
    elif choice == 3:
        position = int(input("Enter position to insert: "))
        data = int(input("Enter data to insert: "))
        DLL.insert_any_pos(position, data)
    elif choice == 4:
        DLL.delete_first()
    elif choice == 5:
        DLL.delete_last()
    elif choice == 6:
        position = int(input("Enter position to delete: "))
        DLL.delete_any_pos(position)
    elif choice == 7:
        data = int(input("Enter data to search: "))
        DLL.search(data)
    elif choice == 8:
        print("\n")
        DLL.print_list()
    elif choice == 9:
        break
    else:
        print("Invalid choice. Please try again.")