class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        n_elements_sum=n*(n+1)/2
        return int(n_elements_sum-sum(nums))
 
