'''
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]


输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]


借鉴这篇文章的思想
https://zhuanlan.zhihu.com/p/93530380
'''



class Solution:
    def __init__(self):
        self.result = []


    def backtrace(self, current_path, candidates, target):
        # 如果和满足target 那么打印出来
        if sum(current_path) == target:
            self.result.append(current_path)
            print(current_path)
            return

        # 如果和超过了 那么排除
        if sum(current_path) > target:
            return

        # 如果和不够 那么遍历继续
        for i in candidates:
            current_path.append(i)
            self.backtrace(current_path, candidates, target)
            current_path.pop()
        return

    def combinationSum(self, candidates, target):
        # 初始化一个当前路径
        current_path = []
        self.backtrace(current_path, candidates, target)
        print(self.result)
        return self.result

s = Solution()
s.combinationSum([2, 3, 5], 8)

