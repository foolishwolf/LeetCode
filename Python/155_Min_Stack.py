class MinStack(object):
    
    class Node():
        value = None
        nextNode = None
        preNode = None
        minValue = None
        def __init__(self, x=None):
            self.value = x
        
    linklist = Node()

    def __init__(self):
        """
        initialize your data structure here.
        """
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        node = self.Node(x)
        self.linklist.nextNode = node
        if x < self.linklist.minValue or self.linklist.minValue == None:
            curMinValue = x
        else:
            curMinValue = self.linklist.minValue
        topNode = self.linklist
        self.linklist = node
        self.linklist.preNode = topNode
        self.linklist.minValue = curMinValue

    def pop(self):
        """
        :rtype: void
        """
        self.linklist = self.linklist.preNode
        self.linklist.nextNode = None
        self.linklist.value

    def top(self):
        """
        :rtype: int
        """
        return self.linklist.value

    def getMin(self):
        """
        :rtype: int
        """
        return self.linklist.minValue