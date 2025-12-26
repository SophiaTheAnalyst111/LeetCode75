class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i,j = len(word1), len(word2)
        a,b = 0,0
        while a< i and b < j:
            result.append(word1[a])
            result.append(word2[b])
            a += 1
            b += 1
        result.append(word1[a:])
        result.append(word2[b:])
        return "".join(result)
