class Solution(object):
    def vowelConsonantScore(self, s):
        v=0
        c=0
        n = len(s)

        for i in range(n):
            if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
                v+=1
            
            elif 'a' <= s[i] <= 'z':
                c+=1
            
        if c == 0:
            return 0

        score = v//c
        return score


        """
        :type s: str
        :rtype: int
        """
        