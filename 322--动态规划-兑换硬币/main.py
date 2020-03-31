'''
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
'''
import sys
from typing import List

class Solution:
    def __init__(self):
        self.min = sys.maxsize
        self.res_dict = {}

    def coinChange(self, coins: List[int], amount: int) -> int:
        # 此处加入了res_list备忘录 存中间的计算结果
        print(coins)
        def DP(amount):
            res = self.min
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            if amount in self.res_dict:
                return self.res_dict[amount]

            for coin in coins:
                sub_problem = DP(amount-coin)
                if sub_problem == -1:
                    continue
                res = min(res, 1+sub_problem)
            if res == self.min:
                return -1
            self.res_dict[amount] = res
            return res

            # 此时选出了最小值

        res = DP(amount)
        return res


s = Solution().coinChange([1,2,5], 11)
print(s)

