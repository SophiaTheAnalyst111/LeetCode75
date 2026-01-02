class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flo = [0] + flowerbed + [0]
        for i in range(1, len(flo)-1):
            if flo[i -1] == 0 and flo[i] == 0 and flo[i + 1] == 0:
                flo[i] = 1
                n -= 1
        if n > 0:
            return False
        else:
            return True
        