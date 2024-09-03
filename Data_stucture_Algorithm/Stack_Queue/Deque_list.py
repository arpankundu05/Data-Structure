# Deque using list--

class Deque:
    def __init__(self):
        self.items=[]

    def insert_front(self,data):
        self.items.insert(0,data)
        return
    
    def insert_rear(self,data):
        self.items.append(data)
        return
    
    def delete_front(self):
        if len(self.items)==0:
            print("\nNo data avaliable to delete!!")
            return
        else:
            self.items.pop(0)
            return
    
    def delete_rear(self):
        if len(self.items)==0:
            print("\nNo data avaliable to delete!!")
            return
        else:
            self.items.pop(-1)
            return
    
    def front(self):
        if len(self.items)==0:
            print("\nNo front value!!")
        else:
            print(self.items[0])
            return
    
    def rear(self):
        if len(self.items)==0:
            print("\nNo rear value!!")
        else:
            print(self.items[-1])
            return
    
    def search(self,data):
        if len(self.items)==0:
            print("\nNo data exist to search!!")
            return
        else:
            for i in self.items:
                if i==data:
                    print("\nSearch Succesfull..")
                    return
            else:
                print("\nSearch Un-succesfull!!")
                return
            
    
    def count(self):
        pass
    
    def print_data(self):
        if len(self.items)==0:
            print("\nNo data avaliable to print!!")
            return
        else:
            print("\n")
            for i in self.items:
                print(i,end=" ")
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