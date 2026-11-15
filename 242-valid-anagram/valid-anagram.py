class Solution(object):
    def isAnagram(self, s, t):
        c= list(s)
        d=list(t)

        c.sort()
        d.sort()

        if c==d:
            return True
        else:
            return False



        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        