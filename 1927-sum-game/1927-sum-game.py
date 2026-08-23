class Solution:
    def sumGame(self, nums):
        n = len(nums)

        leftsum = 0
        rightsum = 0
        leftcount = 0
        rightcount = 0

        for i in range(n):
            if nums[i] == '?':
                if i < n // 2:
                    leftcount += 1
                else:
                    rightcount += 1
            else:
                if i < n // 2:
                    leftsum += int(nums[i])
                else:
                    rightsum += int(nums[i])

        if (rightcount + leftcount) % 2 == 1:
            return True

        rightsum = 2 * rightsum + rightcount * 9
        leftsum = 2 * leftsum + leftcount * 9

        return rightsum != leftsum