class Solution(object):
    def differenceOfSum(self, nums):
        n = len(nums)

        elSum=sum(nums)
        digitSum = 0

        for num in nums:
            temp = num
            while temp>0:
                digitSum += temp%10
                temp = temp // 10  
        
        return abs(elSum - digitSum)
        """
        :type nums: List[int]
        :rtype: int
        """
        