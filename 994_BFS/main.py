from typing import List


# 对腐烂的橘子 进行广搜
class pos(object):
    def __init__(self, i, j, minute):
        self.row = i
        self.col = j
        self.minute = minute

class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:

        from queue import Queue
        q = Queue()
        row = len(grid)
        col = len(grid[0])
        minute = 0
        # 将所有的腐烂的橘子都放到队列中
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    item = pos(i, j, minute)
                    q.put(item)
        directs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        while not q.empty():
            p = q.get()
            minute = p.minute
            for direct in directs:
                i = p.row + direct[0]
                j = p.col + direct[1]
                if i >= row or i < 0 or j >= col or j < 0:
                    continue
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    item = pos(i, j, minute+1)
                    q.put(item)
        for line in grid:
            if 1 in line:
                return -1
        return minute

s = Solution()
# res = s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
# res = s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
res = s.orangesRotting([[0, 2]])
print(res)