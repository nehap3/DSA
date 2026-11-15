class Solution(object):
    def mostWordsFound(self, sentences):
        maxWord = 0

        for sentence in sentences:
            wordLength = len(sentence.split())
            
            if wordLength>maxWord:
                maxWord= wordLength
        
        return maxWord

        """
        :type sentences: List[str]
        :rtype: int
        """
        