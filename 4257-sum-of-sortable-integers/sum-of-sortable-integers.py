class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        
        # 1. Prefix count of adjacent drops
        drops = [0] * n
        for i in range(1, n):
            drops[i] = drops[i - 1] + (1 if nums[i - 1] > nums[i] else 0)
            
        def count_drops(l: int, r: int) -> int:
            """Return number of drops in nums[l..r]."""
            return drops[r] - drops[l]

        # 2. Block min/max precomputation
        # To quickly check max(block_i) <= min(block_{i+1})
        ans = 0
        
        for k in range(1, n + 1):
            if n % k != 0:
                continue
                
            valid = True
            prev_max = -1
            
            for start in range(0, n, k):
                end = start + k - 1
                
                # Count drops within the current block
                block_drops = count_drops(start, end)
                
                if block_drops > 1:
                    valid = False
                    break
                elif block_drops == 1:
                    # If there's 1 drop, wrap-around condition must hold
                    if nums[end] > nums[start]:
                        valid = False
                        break
                
                # Check block elements vs previous block's maximum
                block_min = min(nums[start:start + k])
                block_max = max(nums[start:start + k])
                
                if prev_max > block_min:
                    valid = False
                    break
                    
                prev_max = block_max
            
            if valid:
                ans += k
                
        return ans