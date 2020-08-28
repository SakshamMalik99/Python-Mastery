#function to add element at the end of list
def push(stack,x):
    stack.append(x)
#function to remove last element from list    
def pop(stack):
    n = len(stack)
    if(n<=0):
        print("Stack empty....Pop not possible")
    else:
        stack.pop()

#function to display stack entry
def display(stack):
    if len(stack)<=0:
        print("Stack empty...........Nothing to display")
    for i in stack:
        print(i,end=" ")
#main program starts from here 
x=[]
choice=0
while (choice!=4):
    print("\n\t\t\t stack menu \n\t1. push \n\t2. pop \n\t3. Display \n\t4. Exit")
    choice = int(input("Enter your choice"))
    
    if(choice==1):
        value = int(input("Enter value "))
        push(x,value)
    if(choice==2):
        pop(x)
    if(choice==3):
        display(x)
    if(choice==4):
        print("You selected to close this program")
    
