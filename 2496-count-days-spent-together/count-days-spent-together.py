class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]

        def toDays(date):
            month, day = map(int, date.split('-'))
            return sum(days[:month - 1]) + day

        a1 = toDays(arriveAlice)
        a2 = toDays(leaveAlice)
        b1 = toDays(arriveBob)
        b2 = toDays(leaveBob)

        return max(0, min(a2, b2) - max(a1, b1) + 1)
        