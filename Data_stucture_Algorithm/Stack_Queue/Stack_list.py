# Stack using list

class stack:
    def __init__(self):
        self.items=[]
    
    # To add an data in stack
    def push(self,data):
        self.items.append(data)

    # To delet an elemnt--
    def pop(self):
        if len(self.items)==0:
            print("\nNo data avaliable to delete!")
            return
        else:
            self.items.pop(-1)
            
    # To know the last element-
    def peek(self):
        if len(self.items)==0:
            print("\nNo data avaliable!!")
            return
        else:
            print(self.items[-1])
            
    # To search an element--
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
    
    # To count data--
    def count(self):
        print("\n",len(self.items))
        return
    
    # To print the stack--
    def print_stack(self):
        if len(self.items)==0:
            print("\nNo data avaliable to print!!")
            return
        else:
            print("\n")
            for i in self.items:
                print(i,end=" ")
        print("\n")
        
mystack=stack()
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
        mystack.print_stack()
    elif choice==6:
        mystack.count()
    elif choice==7:
        break
    else:
        print("Wrong choice!!")