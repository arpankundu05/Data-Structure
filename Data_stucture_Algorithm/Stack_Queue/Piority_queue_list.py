# Piority Queue using list--

class Piority_queue:
    def __init__(self):
        self.items=[]
    
    # Push an element
    def push(self, data):
        if len(self.items) == 0:
            self.items.append(data)
            return
        else:
            for i in range(len(self.items)):
                if data < self.items[i]:
                    self.items.insert(i, data)
                    return
            self.items.append(data)
    
    # Delete an element 
    def pop(self):
        if len(self.items)==0:
            print("\nNo data avaliable to delete!!")
            return
        else:
            self.items.pop(-1)
            return
        
    # To print peek value
    def peek(self):
        if len(self.items)==0:
            print("\nNo peek value!!")
            return
        else:
            print("\n",self.items[-1])
            return
      
    # Search for an element  
    def search(self,data):
        if len(self.items)==0:
            print("\nNo data exist to search!!")
            return
        else:
            for i in self.items:
                if i==data:
                    print("\nSearch Succsfull..")
                    return
            else:
                print("\nSearch Un-succesfull!!")
                return
    
    # Print the data
    def print_data(self):
        if len(self.items)==0:
            print("\nNo data exist to print!!")
            return
        else:
            print("\n")
            for i in self.items:
                print(i,end=" ")
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