class Solution(object):
    def checkIfPangram(self, sentence):
        return all(char in sentence for char in 'abcdefghijklmnopqrstuvwxyz')

        


        """
        :type sentence: str
        :rtype: bool
        """
        