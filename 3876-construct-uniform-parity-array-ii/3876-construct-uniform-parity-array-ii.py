class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        smallest = min(nums1)
        if smallest % 2 == 1:
            return True
        for num in nums1: 
            if num % 2 == 1:
                return False
        return True