class Solution(object):
    def xorOperation(self, n, start):
        ans = 0

        for i in range(n):
            num = start+2*i
            ans^=num
        return ans
        
       
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        