#Class:
#Set or category of things having some property or attribute in common and differentiated from others by a kind, type, or quality
#Blueprint for individual objects with exact behaviour
#
#Object:
#One of the instances of the class
#Self: Represents the instance of the class.
#By using "self" keyword we can access the attributes and methods of the class in Python.
# Always put self as the first argument
#Colon: Indication of a code block
#__init__: CONSTRUCTOR. 

#Base class
class Chain():
    _max_size = 100 #Class variable

    # *** Class Methods

    @staticmethod #a "decorator" just to remind us that this is a class method and hence has no "self"
    def size_limit(): return Chain._max_size

    #def make(items=[]): #Also a cclass method (without staticmethod decorator)
    #  return Chain(items)

    # **** Instance methods

    def __init__(self, init_links=[]):
        self.links = init_links.copy()

    def get_links(self): return self.links
    
    def pp(self):
        for index in range(len(self.links)):
            print(index, " : ", self.links[index])
    def len(self): return len(self.links)

    def add(self, item):
        if self.len() < Chain._max_size:
            self.links.append(item) #Always adds to the end of the chain.

    def pop(self):
        return self.links.pop() #remove and return last item of teh chain

    def join(self,chain2):
        if self.len() + chain2.len() <= Chain._max_size:
            self.links.extend(chain2.get_links())
    
    def copy(self):
        return type(self)(self.links) #Should work for Chain or any of the subclasses

    # OPERATOR OVERLOADING (=== < + ...)

    def __eq__(self,c2):
        return type(self) == type(c2) and self.links == c2.links
    
    def __gt__(self,c2):  
        return type(self.links) > c2.links #greater than
    
    def __str__(self):
        return str(self.links) #same as self.links__str__()
    
    def __repr__(self):
        return str(type(self)) + " links:" + str(self)

    def __add__(self, c2):
        return Chain(self.links + c2.links)


class Stack(Chain):
    def __init__(self, init_links=[]):
        Chain.__init__(self,init_links) #Use superclass init
    
    def push(self,item): self.add(item)

#**************** QUEUE *******************************
class Queue(Chain):
    def __init__(self,init_links=[]):
        Chain.__init__(self,init_links)
    
    def push(self,item):
        if self.len() < Queue._max_size:
            self.links.insert(0,item)

#******************

class Series(Chain):
    def __init__(self,init_links=[]):
        #Chain.init(self,init_links)
        self.currloc = -1
    
    # def get currloc(self):
    #     return self.currloc
    
    def insert(self,index,item):
        if self.len() < self._max_size:
            self.links.insert(index,item)
    
    def delete(self,index):
        if index < self.len():
            del self.links[index]  #using Python's del statement
    
    def update(self,index,item):
        self.links[index] = item
    
    def next(self):
        self.currloc += 1
        return self.links[self.currloc] if self.currloc < self.len() else None

        