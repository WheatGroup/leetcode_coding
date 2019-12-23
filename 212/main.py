from Trie import Trie
# 引入前缀树

# 所用知识点是 前缀树和深度优先遍历
words = ["oath", "pea", "eat", "rain", "eathi", "etax", "axasx", "vlfi", "nerv"]
board = [
          ['o','a','a','n'],
          ['e','t','a','e'],
          ['i','h','k','r'],
          ['i','f','l','v']
        ]

class Solution79:
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


trie = Trie()
import time
begin = time.clock()
for word in words:
    # 先使用纯循环 dfs 遍历
    s = Solution79()
    result = s.exist(board, word)

end = time.clock()
print(end - begin)



class Solution212:
    # 从board中用dfs 搜索word
    def exist(self, board, words):
        # 建立前缀树
        for word in words:
            # 显示用前缀树存储单词列表 然后再dfs
            trie.insert(word)
        # 然后遍历board 看组成的前缀是否在前缀树中 不在的话就return
        board_w = len(board[0])
        board_h = len(board)
        marked = [[0] * board_w for i in range(board_h)]
        # 对应方向的 上右下左
        re_list = []

        def find_word(col, row, s):
            # 超出范围或者遍历过 就退出
            if (row < 0 or row >= len(board)) or (col < 0 or col >= len(board[row])) or marked[row][col]:
                return False

            s += board[row][col]
            # 每次这个循环 都要从首字母开始 也就是word[0]开始
            if not trie.startsWith(s):
                return False

            if trie.search(s):
                # search到了 代表完整的单词都在 而不是只有前缀在
                re_list.append(s)
            # 因为是深搜 所以需要一条支线走到底 直到那个支线的四个方向都不行了之后 标记为0
            marked[row][col] = 1
            if find_word(row - 1, col, s):
                return True
            if find_word(row + 1, col, s):
                return True
            if find_word(row, col - 1, s):
                return True
            if find_word(row, col + 1, s):
                return True
            marked[row][col] = 0

        for i in range(board_h):
            for j in range(board_w):
                s = ''
                res = find_word(i, j, s)
                if res:
                    return True
        return False

begin = time.clock()
s = Solution212()
result = s.exist(board, words)
end = time.clock()
print(end - begin)








