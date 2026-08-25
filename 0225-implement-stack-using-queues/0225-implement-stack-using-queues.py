class MyStack(object):

    def __init__(self):
        # Use instance variables
        self.q1 = []
        self.q2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.pop(0))
        # Swap references
        self.q1, self.q2 = self.q2, self.q1    

    def pop(self):
        """
        :rtype: int
        """
        return self.q1.pop(0)

    def top(self):
        """
        :rtype: int
        """
        return self.q1[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q1) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()