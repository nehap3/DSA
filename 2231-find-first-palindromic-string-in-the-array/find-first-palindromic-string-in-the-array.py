class Solution(object):
    def firstPalindrome(self, words):
        wordOcc = 0

        for word in words:
            if word==word[::-1]:
                return word
        
        return ""

        """
        :type words: List[str]
        :rtype: str
        """
        