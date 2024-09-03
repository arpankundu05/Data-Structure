# Create a node class for creating a node
class Node:
    def __init__(self, item=None, next=None, prev=None):
        self.item = item
        self.next = next
        self.prev = prev

# Create Circular Doubly Linked List
class Circular_Doubly_Linked_List:
    def __init__(self, last=None):
        self.last = last

    # Insert a node at the start
    def insert_at_start(self, data):
        newnode = Node(data)
        if self.last is None:
            self.last = newnode
            newnode.next = newnode
            newnode.prev = newnode
        else:
            newnode.next = self.last.next
            newnode.prev = self.last
            self.last.next.prev = newnode
            self.last.next = newnode

    # Insert a node at the end
    def insert_at_last(self, data):
        newnode = Node(data)
        if self.last is None:
            self.last = newnode
            newnode.next = newnode
            newnode.prev = newnode
        else:
            newnode.next = self.last.next
            newnode.prev = self.last
            self.last.next.prev = newnode
            self.last.next = newnode
            self.last = newnode

    # Insert a node at any position
    def insert_any_position(self, pos, data):
        if pos < 0:
            print("\nInvalid position")
            return
        elif pos == 0:
            self.insert_at_start(data)
            return
        else:
            temp = self.last.next
            newnode = Node(data)
            for i in range(pos - 1):
                temp = temp.next
                if temp == self.last.next:
                    print("\nPosition out of range")
                    return
            newnode.next = temp.next
            newnode.prev = temp
            temp.next.prev = newnode
            temp.next = newnode
            if temp == self.last:
                self.last = newnode

    # Delete the first node
    def delete_at_start(self):
        if self.last is None:
            print("\nNothing to be deleted")
            return
        else:
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next
                self.last.next.prev = self.last

    # Delete the last node
    def delete_at_last(self):
        if self.last is None:
            print("\nNothing to be deleted")
            return
        else:
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.prev.next = self.last.next
                self.last.next.prev = self.last.prev
                self.last = self.last.prev

    # Delete a node at any position
    def delete_any_position(self, pos):
        if pos < 0:
            print("\nInvalid position")
            return
        elif pos == 0:
            self.delete_at_start()
            return
        else:
            temp = self.last.next
            for i in range(pos):
                temp = temp.next
                if temp == self.last.next:
                    print("\nPosition out of range")
                    return
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            if temp == self.last:
                self.last = temp.prev

    # Search for an element in the list
    def search(self, data):
        if self.last is None:
            print("\nSearch Unsuccessful!!")
            return
        else:
            temp = self.last.next
            while temp != self.last:
                if temp.item == data:
                    print("\nSearch Successful..")
                    return
                temp = temp.next
            if temp.item == data:
                print("\nSearch Successful..")
            else:
                print("\nSearch Unsuccessful!!")

    # Print the list
    def print_list(self):
        if self.last is None:
            print("\nNothing to be printed!!")
            return
        else:
            temp = self.last.next
            while temp != self.last:
                print(temp.item, end=" ")
                temp = temp.next
            print(temp.item)


CDLL=Circular_Doubly_Linked_List()
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
        CDLL.insert_at_start(data)
    elif choice == 2:
        data = int(input("Enter data to insert at end: "))
        CDLL.insert_at_last(data)
    elif choice == 3:
        pos = int(input("Enter position to insert: "))
        data = int(input("Enter data to insert: "))
        CDLL.insert_any_position(pos, data)
    elif choice == 4:
        CDLL.delete_at_start()
    elif choice == 5:
        CDLL.delete_at_last()
    elif choice == 6:
        position = int(input("Enter position to delete: "))
        CDLL.delete_any_position(position)
    elif choice == 7:
        data = int(input("Enter data to search: "))
        CDLL.search(data)
    elif choice == 8:
        print("\n")
        CDLL.print_list()
    elif choice == 9:
        break
    else:
        print("Invalid choice. Please try again.")