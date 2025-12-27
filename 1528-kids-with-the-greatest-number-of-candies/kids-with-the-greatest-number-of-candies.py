class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        more = False
        for i in range(len(candies)):
            for j in range(len(candies)):
                if candies[i] + extraCandies >= candies[j]:
                    more = True
                else:
                    more = False
                    break
            result.append(more)
        return result

        