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
        self.links = []
        self.is_end = False

    def put(self, ch):

    def get(self, ch, node):

    def



class Trie(object):
    def __init__(self):
        self.root = {}
        self.

    def insert(self, word: str) -> None:

    def search(self, word: str) -> None:

