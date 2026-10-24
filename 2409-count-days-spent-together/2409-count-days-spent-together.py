class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str,
                          arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]

        def to_days(date):
            month, day = map(int, date.split('-'))
            return sum(days[:month - 1]) + day

        start = max(to_days(arriveAlice), to_days(arriveBob))
        end = min(to_days(leaveAlice), to_days(leaveBob))

        if start > end:
            return 0

        count = 0
        for day in range(start, end + 1):
            count += 1

        return count