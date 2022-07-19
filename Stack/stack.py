import gc

class _Node:
    def __init__(self, data, previous):
        self.data = data
        self.previous = previous


class Stack:
    def __init__(self):
        self.top = None
        
    #Observers     
    def is_empty(self):
        return self.top == None
      
    #Observers    
    def peek(self):
        if Stack.is_empty(self):
            raise Exception("Stack is empty")
        return self.top.data
      
    #Constructors    
    def push(self, data):
        self.top = _Node(data, self.top)
        
    #Destroyers
    def pop(self):
        if Stack.is_empty(self):
            raise Exception("Stack is empty")
        popped = self.top.data
        x = self.top
        self.top = self.top.previous
        del x
        gc.collect()
        return popped
      
    #Special
    def __len__(self):
        temp = self.top
        amount = 0
        while(temp):
            amount += 1
            temp = temp.previous
        return amount

    
    
################ SIMPLEST IMPLEMTATION #################
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
	    if not self.is_empty():
		    return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items