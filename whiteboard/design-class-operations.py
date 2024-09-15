# Problem: Design a class that does this:
# Insert an element (without duplicates)
# Remove an element
# Return a random element that was already inserted (with equal probability)
# random.choice(list)

## 20h10
## set
## empty structure > just return
## only integers in the input > positive and negative numbers
## just one element to insert and to remove
## for random element I was thinking about using the length of my structure and using random function to choose the number

## 20h20
## input = {1}

from inspect import stack
import random
from typing import Set


class Store:
   def __init__(self):
     self.set = Set()


   def insertElement(self, input):
      self.set.add(input) ## O(1)
     
   def removeElement(self, input):
      self.set.remove(input) ## O(n)

   def randomElement(self):
       list_aux = list(self.set) ##O(n)
       return random.choice(list_aux)

# 20h50

# Follow-up: Make every operation to be O(1) 




class Store:
   def __init__(self):
     self.hashMap = {}
     self.stack = []

   def insertElement(self, input):
     if self.existElement(input) != True:
        self.stack.append(input)
        self.hashMap[input] = len(self.stack) - 1 ## O(1)

## input = {4}
## stack = [1, 2, 4, 5, 6]
## len(stack) = 4
## hashMap = {"1": "0", "2": "1", "4": "2", "5": "3","6": "4"}
## hashMap = {"4": "2","6": "4"}

## stack = [1, 2, 6, 5, 4] ## stack = [1, 2, 6, 5]
## hashMap = {"1": "0", "2": "1", "6": "2", "5": "3","4": "4"}

## input = {4}
## stack = [1, 2, 6, 5]
## hashMap = {"1": "0", "2": "1", "6": "2", "5": "3","4": None}
   def existElement(self,input):
      if (input in self.hashMap):
        return True

   def swapElement(self,input):
     if self.existElement(input) == True:
       index_value = self.hashMap[input]  ##index_value = None
       last_value = stack[len(stack)-1]  ## last_value = 5
      
       self.hashMap[input] = len(self.stack) - 1  ## "4": "3"
       self.hashMap[last_value] = index_value      ## "5": "None"
  
       self.stack[index_value], self.stack[len(self.stack) - 1] = self.stack[len(self.stack) - 1], self.stack[index_value]
     
     
   def removeElement(self, input):
     if self.existElement(input) == True:
       self.swapElement(input)
       self.stack.pop()
       del(self.hashMap[input])  ## O(1)

   def randomElement(self):
       return random.choice(self.stack) ## O(1)



# Test case:
# Insert(1), Insert(4), Insert(4), remove(4), remove(4), random()

class Store:
    def __init__(self):
     self.hashMap = {}
     self.stack = []
    ## stack = [1]
    ## hashMap = {"1": 0} 
    def insertElement(self, input):
        if self.existElement(input) != True:
            self.stack.append(input)
            self.hashMap[input] = len(self.stack) - 1 ## O(1)

    def existElement(self,input):
        if (input in self.hashMap):
            return True

    def swapElement(self,input):
        if self.existElement(input) == True:
            index_value = self.hashMap[input]  ##index_value = 1
            last_value = stack[len(stack)-1]  ## last_value = 4
            
            self.hashMap[input] = len(self.stack) - 1  ## "4": "1"
            self.hashMap[last_value] = index_value      ## "4": "1"
        
            self.stack[index_value], self.stack[len(self.stack) - 1] = self.stack[len(self.stack) - 1], self.stack[index_value] ##
        
        
    def removeElement(self, input):
        if self.existElement(input) == True:
            self.swapElement(input)
            self.stack.pop()
            del(self.hashMap[input])  ## O(1)

    def randomElement(self):
        return random.choice(self.stack) ## O(1)

