class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Calculate the square of each element
        squares = [x * x for x in nums]
        squares.sort()
        
        n = len(nums)
        half = n // 2
        
        # Smallest 'half' elements are subtracted, largest 'n - half' elements are added
        return sum(squares[half:]) - sum(squares[:half])        