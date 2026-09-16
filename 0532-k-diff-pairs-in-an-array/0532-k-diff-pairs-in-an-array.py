class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pair = set()
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if abs(nums[i] - nums[j]) == k:
                    a, b = nums[i], nums[j]
                    if a > b:
                        a, b = b, a
                    pair.add((a, b))
        return len(pair)
