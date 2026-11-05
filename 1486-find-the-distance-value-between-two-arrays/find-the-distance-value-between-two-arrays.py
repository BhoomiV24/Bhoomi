import bisect
class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        count = 0
        
        for val in arr1:
            # Find the position where `val - d` would be inserted
            idx = bisect.bisect_left(arr2, val - d)
            
            # If idx is within bounds and the element at idx is <= val + d,
            # then there is an element in arr2 within distance d of val.
            if idx < len(arr2) and arr2[idx] <= val + d:
                continue
                
            count += 1
            
        return count      