class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #Sophia Singh optimized solution
        result = []
        max_candies = max(candies)
        for candy in candies:
            result.append(candy + extraCandies >= max_candies)
        return result

        