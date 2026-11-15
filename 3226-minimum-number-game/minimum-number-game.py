class Solution(object):
    def numberGame(self, nums):
    
        nums.sort()
        n= len(nums)
        arr= []

        for i in range(0,n,2):
            arr.append(nums[i+1])
            arr.append(nums[i])
        
        return arr

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        