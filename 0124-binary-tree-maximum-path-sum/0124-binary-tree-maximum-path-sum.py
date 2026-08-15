class Solution:

    def __init__(self):
        self.maxSum = float('-inf')

    def maxPathSum(self, root):

        def findMax(node):

            if not node:
                return 0

            left = max(0, findMax(node.left))
            right = max(0, findMax(node.right))

     
            currentPath = left + node.val + right

            self.maxSum = max(self.maxSum, currentPath)

            return node.val + max(left, right)

        findMax(root)

        return self.maxSum