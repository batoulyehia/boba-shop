#Let's try implementing Stack and Queue using Python!

#make a simple stack and then after that you should use the thing for the thing i mean 
#create classes lmao
#ok let's get started

bobaStack = []
#push
bobaStack.append("Honeydew")
bobaStack.append("Strawberry")
bobaStack.append("Milk Tea")
bobaStack.append("Taro")
#print(bobaStack)

#pop 
lastFlavor = bobaStack.pop()
#print(lastFlavor)


#isEmpty(bobaStack)

class Stack():
    def __init__(self):
        self.items=[]
        #initializes a stack object to an empty list
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        if(len(self.items) > 0):
            print("There are still bobas in your stack!")
        else:
            print("Stack empty")

#This is a class of all of the customers waiting to get their bubble tea. 
class Queue:
    def __init__(self):
        self.customers=[]
    
    def enqueue(self,customer):
        self.customers.insert(0, customer)
    def dequeue(self):
        return self.customers.pop()

    def isEmpty(self):
        if(len(self.customers) > 0):
            print("STILL HAVE CUSTOMERS")
        else:
            print("yo we're all out of customers try to get ppls attention")
        

bobas = Stack()
bobas.push("Strawberry Milk Tea")
bobas.push("Milk Tea")
bobas.push("Tapioca-less bubble tea")
bobas.push("Honey Dew")
bobas.push("Cheesecake")
print(bobas.items)
bobas.pop()
print(bobas.items)
bobas.isEmpty()