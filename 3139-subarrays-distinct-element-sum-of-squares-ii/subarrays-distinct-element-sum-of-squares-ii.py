
class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.sum_d = [0] * (4 * n)
        self.sum_sq = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def _push(self, node, start, end):
        if self.lazy[node] != 0:
            v = self.lazy[node]
            mid = (start + end) // 2
            left_len = mid - start + 1
            right_len = end - mid

            left = 2 * node
            right = 2 * node + 1

            # Update left child
            self.sum_sq[left] += 2 * v * self.sum_d[left] + v * v * left_len
            self.sum_d[left] += v * left_len
            self.lazy[left] += v

            # Update right child
            self.sum_sq[right] += 2 * v * self.sum_d[right] + v * v * right_len
            self.sum_d[right] += v * right_len
            self.lazy[right] += v

            self.lazy[node] = 0

    def update(self, node, start, end, l, r, val):
        if l <= start and end <= r:
            length = end - start + 1
            self.sum_sq[node] += 2 * val * self.sum_d[node] + val * val * length
            self.sum_d[node] += val * length
            self.lazy[node] += val
            return

        self._push(node, start, end)
        mid = (start + end) // 2
        if l <= mid:
            self.update(2 * node, start, mid, l, r, val)
        if r > mid:
            self.update(2 * node + 1, mid + 1, end, l, r, val)

        self.sum_d[node] = self.sum_d[2 * node] + self.sum_d[2 * node + 1]
        self.sum_sq[node] = self.sum_sq[2 * node] + self.sum_sq[2 * node + 1]

    def query_sq(self, node, start, end, l, r):
        if l <= start and end <= r:
            return self.sum_sq[node]

        self._push(node, start, end)
        mid = (start + end) // 2
        res = 0
        if l <= mid:
            res += self.query_sq(2 * node, start, mid, l, r)
        if r > mid:
            res += self.query_sq(2 * node + 1, mid + 1, end, l, r)
        return res

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        st = SegmentTree(n)
        last_pos = {}
        total_sum = 0

        for j, x in enumerate(nums):
            prev = last_pos.get(x, -1)
            # Add 1 to distinct counts for all subarrays starting from indices (prev + 1) to j
            st.update(1, 0, n - 1, prev + 1, j, 1)
            
            # Query sum of squared distinct counts for all valid starting indices 0..j
            total_sum = (total_sum + st.query_sq(1, 0, n - 1, 0, j)) % MOD
            last_pos[x] = j

        return total_sum        