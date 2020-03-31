from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0 for _ in range(num_people)]
        i = 0
        while candies > 0:
            res[i % num_people] += min(i + 1, candies)
            candies -= min(i + 1, candies)
            i += 1
        return res

s = Solution()
res = s.distributeCandies(7, 4)
print(res)