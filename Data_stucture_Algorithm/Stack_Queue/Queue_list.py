# Queue using list--

class Queue:
    def __init__(self):
        self.items=[]
    
    def enqueue(self,data):
        self.items.append(data)
        return
    
    def dequeue(self):
        if len(self.items) == 0:
            print("\nNo data avaliable to delete!!")
            return
        else:
            self.items.pop(0)
            return
    
    def front(self):
        if len(self.items) == 0:
            print("\nNo Front value!")
            return
        else:
            print(self.items[0])
            return
    
    def rear(self):
        if len(self.items)==0:
            print("\nNo rear value!")
            return
        else:
            print(self.items(-1))
            return
    
    def search(self,data):
        if len(self.items)==0:
            print("\nNo data avaliable to search!")
            return
        else:
            # print("\n")
            for i in self.items:
                if i==data:
                    print("\nSearch Succesfull..")
                    return
            else:
                print("\nSearch Un-Succesfull!!")
                return
    
    def print_data(self):
        if len(self.items)==0:
            print("\nNo data avaliable to print!!")
            return
        else:
            print("\n")
            for i in self.items:
                print(i,end=" ")
            print("\n")

myqueue=Queue()
while True:
    print("\n1. enqueue an element")
    print("2. dequeue an element")
    print("3. Front element print")
    print("4. Rear element print")
    print("5. Search an element")
    print("6. Print the Queue")
    print("7. Exit")
    
    choice=int(input("\nEnter your choice: "))
    
    if choice==1:
        data=int(input("Enter the data to insert: "))
        myqueue.enqueue(data)
    elif choice==2:
        myqueue.dequeue()
    elif choice==3:
        myqueue.front()
    elif choice==4:
        myqueue.rear()
    elif choice==5:
        data=int(input("Enter data to search: "))
        myqueue.search(data)
    elif choice==6:
        myqueue.print_data()
    elif choice==7:
        break
    else:
        print("Wrong choice!!")