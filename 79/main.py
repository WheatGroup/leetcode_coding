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



class Solution:
    def exist(self, board, word):
        # 从board 词盘中搜索word这个单词的开头 如果然后开始递归查找后面的字母
        if not board and not board[0]:
            return False

        board_w = len(board[0])
        board_h = len(board)
        marked = [[0] * board_w for i in range(board_h)]
        # 对应方向的 上右下左
        def find_word(row, col, index):
            # 因为匹配到了字母index就会加一  所以index超过word的时候 就是完全匹配上了
            if index == len(word):
                return True
            # 先保证下标在范围内
            if (row < 0 or row >= board_h) or (col < 0 or col >= board_w):
                return False
            # 再看是否字符是否相等
            if board[row][col] != word[index]:
                return False
            # 看是否走过
            if marked[row][col] != 0:
                return False
            # 此节点均符合要求  那边标记为1  然后开始上下左右遍历
            marked[row][col] = 1
            index += 1
            if find_word(row-1, col, index):
                return True
            if find_word(row+1, col, index):
                return True
            if find_word(row, col-1, index):
                return True
            if find_word(row, col+1, index):
                return True

            #   上下左右都没有找到
            marked[row][col] = 0
            return False

        for i in range(0, board_h):
            for j in range(0, board_w):
                if find_word(i, j, 0):
                    return True

        return False



s = Solution()
result1 = s.exist(board, 'ABCCED')
print(result1)
result2 = s.exist(board, 'SEE')
print(result2)
result3 = s.exist(board, 'ABCB')
print(result3)








