# 深度优先遍历

# 定义四个方向  上右下左

board = [
          ['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E']
        ]
# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.

# 初始化一个待标记的数组
board_w = len(board[0])
board_h = len(board)
marked = [[0] * board_w for i in range(board_h)]
#对应方向的 上右下左
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Solution:
    def exist(self, board, word):
        # 从board 词盘中搜索word这个单词的开头 如果然后开始递归查找后面的字母

        for i in range(board_h):
            for j in range(board_w):
                # 每次这个循环 都要从首字母开始 也就是word[0]开始
                index = 0
                if board[i][j] == word[index]:
                    marked[i][j] = 1
                    index += 1
                    # 第四个参数是index = 1 代表 继续匹配 word[1:]单词
                    res = self.backtrace(marked, board, word, index, i, j)
                    if res == True:
                        return True
                    else:
                        marked[i][j] = 0
        return False


    def backtrace(self, marked, board, word, index, i, j):
        if index >= len(word):
            return True
        for direct in directions:
            # 此处不能在 i += direct[0]的情况下进行 这样就在本次递归下修改了坐标 不对
            temp_i = i + direct[0]
            temp_j = j + direct[1]
            if temp_i >= 0 and temp_j >= 0 and temp_i < board_h and temp_j < board_w and board[temp_i][temp_j] == word[index]:
                # 超过了边界
                if marked[temp_i][temp_j] == 1:
                    continue
                marked[temp_i][temp_j] = 1
                index += 1
                res = self.backtrace(marked, board, word, index, temp_i, temp_j)
                if res == True:
                    return True
                else:
                    marked[temp_i][temp_j] = 0
        return False


s = Solution()
result1 = s.exist(board, 'ABCCED')
print(result1)
result2 = s.exist(board, 'SEE')
print(result2)
result3 = s.exist(board, 'ABCB')
print(result3)








