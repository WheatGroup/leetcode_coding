import sys
class Solution:
    def __init__(self):
        self.minDist = sys.maxsize
        self.len1 = 0
        self.len2 = 0


    def EditDist(self, i, j, dist):
        # 代表 通过dist个编辑距离 第一个字符串i之前的部分已经和 第二个字符串j之前的部分一样了
        if i == self.len1:
            # 代表运行到了第一个字符串的最后面的一个字符+1  所以剩下的第二个字符串字节数就是剩下的编辑距离
            dist += (self.len2 - j)




    def oneEditAway(self, first: str, second: str) -> bool:
        self.len1 = len(first)
        self.len2 = len(second)
        self.EditDist(0, 0, 0)

        return self.minDist == 1