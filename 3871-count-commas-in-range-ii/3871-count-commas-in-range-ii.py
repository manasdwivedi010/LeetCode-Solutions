
class Solution:
    def countCommas(self, n):
        ans = 0
        dig = 1000

        while dig <= n:
            ans += n - dig + 1
            dig = dig * 1000

        return ans


