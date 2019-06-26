class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
            return True
        count = 0
        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 0:
                if i == 0 or i == len(flowerbed) - 1:
                    count += 1
                count += 1
            else:
                if count == 0:
                    continue
                n -= (count - 1 ) // 2
                count = 0
            if n <= 0:
                return True
        if count > 0:
            n -= (count -1 ) // 2
        if n <= 0:
            return True
        return False