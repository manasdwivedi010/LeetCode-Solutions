class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = Counter(nums)
        # if n >1:
        #     return nums
        map={}
        for i in nums:
            map[i]=map.get(i,0) +1
        for i,count in map.items():
            if count>1:
                return i
        



        