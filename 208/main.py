from Trie import Trie
trie = Trie()

trie.insert("apple")
result1 = trie.search("apple")
result2 = trie.search("app")
result3 = trie.startsWith("app")
trie.insert("app")
result4 = trie.search("ap")
print(result1, result2, result3, result4)

