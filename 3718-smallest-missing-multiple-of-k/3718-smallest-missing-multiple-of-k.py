class Solution:
    def missingMultiple(self, nums, k):
        seen = set(nums)

        cur = k
        while cur in seen:
            cur += k

        return cur
        