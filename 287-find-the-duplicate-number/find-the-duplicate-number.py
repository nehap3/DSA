class Solution(object):
    def findDuplicate(self, nums):
    
        n = len(nums)
        nums.sort()
        
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                return nums[i]
                