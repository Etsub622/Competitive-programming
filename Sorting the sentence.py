class Solution:
    def sortSentence(self, s: str) -> str:
        str=s.split(' ')
        str.sort(key=lambda x: int(x[-1]))
        return ' '.join(x[:-1] for x in str)
