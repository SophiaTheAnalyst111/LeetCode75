class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        high = 0
        start = 0
        for i in range(len(gain)):
           
            start += gain[i]
            high = max(start,high)
        return high
