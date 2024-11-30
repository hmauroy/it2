class BinaryTreeNode:
    def __init__(self, value, 
                 lefttree = None, 
                 righttree = None):
        self.value = value      
        self.left = lefttree
        self.right = righttree
        self.level = 0

    # Bruker setter/getters
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value
    
    @property
    def left(self):
        return self.__left 
    
    @left.setter
    def left(self, lefttree):
        self.__left = lefttree 
   
    @property
    def right(self):
        return self.__right        
    
    @right.setter
    def right(self, righttree):
        self.__right = righttree 

    @property
    def level(self):
        return self.__level
    
    @level.setter
    def level(self, level):
        self.__level = level
    
    def __str__(self):
        return self.value
    
    def hasRight(self):
        if self.right == None:
            return False
        return True
        #return self.right != None            
    
    def hasLeft(self):
        if self.left == None:
            return False
        return True
        #return self.left != None
    
    def prefixOrder(self):
        print(str(self.value), ' ')
        if self.hasLeft():
            self.left.prefixOrder()
        if self.hasRight():
            self.right.prefixOrder()
        
    def infixOrder(self):
        if self.hasLeft():
            self.left.infixOrder()
        print(str(self.value), ' ')
        if self.hasRight():
            self.right.infixOrder()
        
    def postfixOrder(self):
        if self.hasLeft():
            self.left.postfixOrder()
        if self.hasRight():
            self.right.postfixOrder()
        print(str(self.value), ' ')
        
    def levelOrder(self):
        from queue import SimpleQueue
        FIFOQueue = SimpleQueue()
        FIFOQueue.put(self)
        self.levelOrderEntry(FIFOQueue)
        while not FIFOQueue.empty():
            node = FIFOQueue.get()
            print(str(node.value), ' ')
                
    def levelOrderEntry(self, queue):
        if queue.empty():
            return
        node = queue.get()
        print(str(node.value), ' ')
        if node.hasLeft():
            queue.put(node.left)
        if node.hasRight():
            queue.put(node.right)
        if node.hasLeft() or node.hasRight:
            self.levelOrderEntry(queue)            

    def __eq__(self, other):   
        if other != None:
            return self.value == other.value
        elif other == None and self.value == None:
            return True
        return False

    def __ne__(self, other):
        if other != None:
            if self.value == None:
                return False
            else:
                return not self.value != other.value
        return True
        
    def __lt__(self, other):
        if other != None:
            return self.value < other.value
        elif other == None and self.value == None:
            return False
        return False
    
    def __le__(self, other):
        if other != None:
            return self.value <= other.value
        elif other == None and self.value == None:
            return False
        return False
               
    def __gt__(self, other):
        if other != None:
            return self.value > other.value
        elif other == None and self.value == None:
            return False
        return False
    
    def __ge__(self, other):
        if other != None:
            return self.value >= other.value
        elif other == None and self.value == None:
            return False
        return False