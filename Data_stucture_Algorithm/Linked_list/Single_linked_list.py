# Code for Single Linked List--

# Create The node
class Node:
	def __init__(self,item=None,next=None):
		self.item=item
		self.next=next

class Single_linked_list:
	def __init__(self,head=None):
		self.head=head

	# Insert an element at the first of the linked list-
	def insert_at_start(self,data):
		newnode=Node(data)
		newnode.data=data
		if self.head==None:
			self.head=newnode
		else:
			newnode.next=self.head
			self.head=newnode
	
	# Insert an element in the last of the linked list-
	def insert_at_last(self,data):
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

	# insert an element at any position of the linked list-
	def insert_any_pos(self,position,data):
		newnode=Node(data)
		if position<0:
			print("Index must be greter equal 0")
			return
		if position==0:
			newnode.next=self.head
			self.head=newnode
			return
		temp=self.head
		prev=None
		index=0
		while temp != None and index<position:
			prev=temp
			temp=temp.next
			index += 1
		prev.next=newnode
		newnode.next=temp
		if index<position:
			print("Out of range!!")
			return
	
	# Insert a value after a data--
	def insert_after_data(self,check,data):
		if self.head==None:
			print("Insert not possible!!")
			return
		newnode=Node(data)
		temp=self.head
		while temp is not None:
			if temp.item==check:
				newnode.next=temp.next
				temp.next=newnode
				return
			temp=temp.next

	# Delete an element from first of the linked list-
	def delete_first(self):
		if self.head==None:
			print("No node avaliable to delet!!")
			return
		else:
			if self.head.next==None:
				self.head=None
			else:
				self.head=self.head.next
	
	# Delete an element from last of the linked list-
	def delete_last(self):
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

	# Delete an element from any position of the linked list-
	def delete_any_pos(self, position):
		if self.head is None:
			print("Nothing to be deleted!!")
			return
		if position == 0:
			self.head = self.head.next
			return
		temp = self.head
		for i in range(position - 1):
			if temp is None or temp.next is None:
				break
			temp = temp.next
		if temp is None or temp.next is None:
			print("Position out of range!!")
			return
		temp.next = temp.next.next
        			
	# Search an element in linked list
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

	# Print the linked list-
	def printlist(self):
		temp=self.head
		if temp is None:
			print("Nothing to be printed!!")
			return
		else:
			while temp is not None:
				print(temp.item,end=" ")
				temp=temp.next
		print("\n")

#  Driver Code
SLL= Single_linked_list()
while True:
	print("\n1. Insert at start")
	print("2. Insert at end")
	print("3. Insert at any position")
	print("4. Insert after a value")
	print("5. Delete first")
	print("6. Delete last")
	print("7. Delete at any position")
	print("8. Search")
	print("9. Print list")
	print("10. Exit")

	choice = int(input("Enter your choice: "))

	if choice == 1:
		data = int(input("Enter data to insert at start: "))
		SLL.insert_at_start(data)
	elif choice == 2:
		data = int(input("Enter data to insert at end: "))
		SLL.insert_at_last(data)
	elif choice == 3:
		position = int(input("Enter position to insert: "))
		data = int(input("Enter data to insert: "))
		SLL.insert_any_pos(position, data)
	elif choice == 4:
		check=int(input("Enter Which after add: "))
		data=int(input("Enter data to insert: "))
		SLL.insert_after_data(check,data)
	elif choice==5:
		SLL.delete_first()
	elif choice == 6:
		SLL.delete_last()
	elif choice == 7:
		position = int(input("Enter position to delete: "))
		SLL.delete_any_pos(position)
	elif choice == 8:
		data = int(input("Enter data to search: "))
		SLL.search(data)
	elif choice == 9:
		print("\n")
		SLL.printlist()
	elif choice == 10:
		break
	else:
		print("Invalid choice. Please try again.")