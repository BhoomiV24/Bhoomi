class Solution:
    def minOperations(self, s: str) -> int:
        # If already sorted, 0 operations needed
        if s == ''.join(sorted(s)):
            return 0
        
        n = len(s)
        # Length 2 string that is not sorted cannot be sorted (proper substring size = 1)
        if n == 2:
            return -1
        
        mn = min(s)
        mx = max(s)
        
        # 1 operation if minimum character is at start OR maximum character is at end
        if s[0] == mn or s[-1] == mx:
            return 1
            
        # 3 operations if max char is ONLY at index 0 AND min char is ONLY at index n-1
        if s[0] == mx and s[-1] == mn and s.count(mx) == 1 and s.count(mn) == 1:
            return 3
            
        # All other cases can be solved in 2 operations
        return 2