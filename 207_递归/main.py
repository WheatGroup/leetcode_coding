# 深搜 判断是否有环
# 表达图 用邻接矩阵表示
# 先根据图来创造出 邻接矩阵的表示
'''
示例 1:

输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。


'''
#https://blog.csdn.net/qq_30796379/article/details/80152406
# 依据上图初始化的图邻接矩阵

class Solution:
    def __init__(self):
        self.flag = False

    def canFinish(self, numCourses, prerequisites):
        # 先创建图
        path = [[0 for i in range(numCourses)] for i in range(numCourses)]
        # 遍历prerequisites 初始化 邻接矩阵
        for a, b in prerequisites:
            path[a][b] = 1
        # 下一步是判断此图是否有环 path存储图的信息 顶点
        def DFS(path, begin):
            visited[begin] = True
            for j in range(numCourses):
                # 如果下一个结点没有被访问过 并且 右边存在
                if j == begin:
                    # 自己连接自己 略过
                    continue
                if path[begin][j] == 1:
                    # 有链接
                    if visited[j] == True:
                        self.flag = True
                        return True
                    else:
                        DFS(path, j)
            visited[begin] = False
            return False

        visited = [False for _ in range(numCourses)]
        for begin in range(numCourses):
            # 每次将一个顶点作为深搜的开始时 都需要将visited重新初始化为False
            # for i in range(numCourses):
            #     visited[i] = False
            res = DFS(path, begin)
            if res == True:
                break

        return self.flag

s = Solution()

# res = s.canFinish(2, [[1,0]])
# res = s.canFinish(2, [[1,0],[0,1]])
# res = s.canFinish(3, [[0,1],[0,2],[1,2]])
res = s.canFinish(8, [[0,1], [0,2], [0,3], [0, 4], [0, 5], [1, 2], [1, 4], [2, 3], [3, 4], [4, 5], [5, 2], [5, 6], [5, 7], [6, 5], [6, 7], [7, 5], [7, 6]])
print(res)





