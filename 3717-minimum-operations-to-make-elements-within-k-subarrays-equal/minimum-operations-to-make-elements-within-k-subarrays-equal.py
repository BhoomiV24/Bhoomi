
from typing import List

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, val):
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def kth(self, k):
        idx = 0
        bit_mask = 1 << (self.n.bit_length() - 1)

        while bit_mask:
            nxt = idx + bit_mask
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            bit_mask >>= 1

        return idx + 1


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        vals = sorted(set(nums))
        m = len(vals)

        rank = {v: i + 1 for i, v in enumerate(vals)}

        bit_count = Fenwick(m)
        bit_sum = Fenwick(m)

        window_sum = 0
        costs = []

        # Build first window and slide.
        for i in range(n):
            v = nums[i]
            r = rank[v]

            bit_count.add(r, 1)
            bit_sum.add(r, v)
            window_sum += v

            if i >= x:
                old = nums[i - x]
                ro = rank[old]

                bit_count.add(ro, -1)
                bit_sum.add(ro, -old)
                window_sum -= old

            if i >= x - 1:
                # Find median (lower median).
                med_rank = bit_count.kth((x + 1) // 2)
                median = vals[med_rank - 1]

                cnt_left = bit_count.query(med_rank)
                sum_left = bit_sum.query(med_rank)

                cnt_right = x - cnt_left
                sum_right = window_sum - sum_left

                cost = (
                    median * cnt_left - sum_left
                    + sum_right - median * cnt_right
                )

                costs.append(cost)

        # DP with O(n) space.
        INF = 10**18

        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]
