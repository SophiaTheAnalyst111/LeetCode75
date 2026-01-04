class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = {}
        for i in arr:
            if i in occurences:
                occurences[i] += 1
            else:
                occurences[i] = 1
        return len(occurences.values()) == len(set(occurences.values()))