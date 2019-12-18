# 实现前缀树
'''

实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
startswith： 是否有某个前缀
search： 是否有某个字符串
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true

'''
class TrieNode(object):
    def __init__(self):
        # 此处不能 self.links = []
        # 因为这样要是从links中按照下标选择字符的时候 会报错
        self.links = [None] * 26
        self.is_end = False

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    def containKeys(self, ch):
        # 判断这个结点是否含有某个字符
        return self.links[ord(ch) - ord('a')] != None

    def setEnd(self):
        self.is_end = True


class Trie(object):
    def __init__(self):
        self.root = TrieNode()


    def insert(self, words):
        node = self.root
        for ch in words:
            if not node.containKeys(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)
        node.setEnd()


    def searchPrefix(self, words):
        # 搜索单词的前缀 返回值是None 或者一个node
        # 只有node的is_end是True的时候 才代表有完整的单词 否则只是前缀
        node = self.root
        for ch in words:
            if node.containKeys(ch):
                node = node.get(ch)
            else:
                return None
        return node


    def search(self, words):
        node = self.searchPrefix(words)
        return node is not None and node.is_end


    def startsWith(self, words):
        node = self.searchPrefix(words)
        return node is not None

    def createByBoard(self, board):
        node = self.root
        if board == []:
            return
        weight = len(board[0])
        height = len(board)
        w = 0
        h = 0
        while w < weight and h < height:
            ch = board[w][h]
            if not node.containKeys(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)









