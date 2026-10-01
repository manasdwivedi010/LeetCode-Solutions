class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs ={')':'(',']':'[','}':'{'}
        for c in s:
            if c in pairs:
                if not stack or stack.pop()!=pairs[c]:
                    return False
            else:
                stack.append(c)
        return not stack            
        