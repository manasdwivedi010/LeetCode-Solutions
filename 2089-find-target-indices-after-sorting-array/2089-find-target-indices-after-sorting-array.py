class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []

        lessThanTargetCount = 0
        targetCount = 0

        for num in nums:
            if num < target:
                lessThanTargetCount += 1

            if num == target:
                targetCount += 1

        for i in range(targetCount):
            ans.append(lessThanTargetCount + i)

        return ans