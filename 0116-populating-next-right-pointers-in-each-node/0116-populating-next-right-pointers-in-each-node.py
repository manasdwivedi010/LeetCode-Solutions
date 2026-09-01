"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        if root is None: return None
        dq, pre_level, pre_node = deque([(1, root)]), 0, None
        while dq:
            level, node = dq.popleft()
            if level == pre_level:  
                pre_node.next = node
                pre_node = node
            else: 
                pre_level, pre_node = level, node
            if node.left:  
                dq.append((level + 1, node.left))
                dq.append((level + 1, node.right))
        return root
