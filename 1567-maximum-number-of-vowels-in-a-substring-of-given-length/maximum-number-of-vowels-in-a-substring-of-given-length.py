class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_count = 0
        count = 0
        vowels =['a','e','i','o','u']
        window = s[:k]
        for i in range(len(window)):
            if window[i] in vowels:
                count += 1
            max_count = count
        
        for i in range(k,len(s)):
            if s[i-k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            if count > max_count:
                max_count = count
        return max_count