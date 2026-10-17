class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x):
            total = 0
            while x:
                total += x % 10
                x //= 10
            return total

        n = len(nums)

        # Sort by digit sum, then by number
        arr = sorted(nums, key=lambda x: (digit_sum(x), x))

        # Map each number to its current index
        pos = {num: i for i, num in enumerate(nums)}

        swaps = 0
        visited = [False] * n

        for i in range(n):
            if visited[i] or pos[arr[i]] == i:
                continue

            # Count the cycle length
            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = pos[arr[j]]
                cycle_size += 1

            if cycle_size > 1:
                swaps += cycle_size - 1

        return swaps       