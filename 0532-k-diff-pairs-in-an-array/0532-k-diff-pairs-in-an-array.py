class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:


        a=0
        c=Counter(nums)
            
        if k==0:
            for key,v in c.items():
                if v>1:
                    a+=1
        else:
            for key,v in c.items():
                if key+k in c:
                    a+=1
        return a
