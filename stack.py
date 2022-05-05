import gc

class Node:
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
    def get_top(self):
        if Stack.is_empty(self):
            raise Exception("Stack is empty")
        return self.top.data
      
    #Constructors    
    def push(self, data):
        self.top = Node(data, self.top)
        
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
