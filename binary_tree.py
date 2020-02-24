"""
    Pre-order, in-order and post-order traversal of binary trees.

    Author: Wenru Dong
"""
from typing import TypeVar, Generic, Generator, Optional

T = TypeVar("T")

class TreeNode(Generic[T]):
    def __init__(self, value: T):
        self.val = value
        self.left = None
        self.right = None
    

# Pre-order traversal
def pre_order(root: Optional[TreeNode[T]]) -> Generator[T, None, None]:
    if root:
        yield root.val
        yield from pre_order(root.left)
        yield from pre_order(root.right)

# In-order traversal
def in_order(root: Optional[TreeNode[T]]) -> Generator[T, None, None]:
    if root:
        yield from in_order(root.left)
        yield root.val
        yield from in_order(root.right)

# Post-order traversal
def post_order(root: Optional[TreeNode[T]]) -> Generator[T, None, None]:
    if root:
        yield from post_order(root.left)
        yield from post_order(root.right)
        yield root.val


# 用栈 把先序遍历的非递归方式写出来
def pre_order_un_fac(root):
    if root == None:
        return []

    # 非递归的方式就需要用栈 存储右子节点
    s = []
    p = root
    while(p or len(s)):
    # 从根结点开始遍历 先序遍历
        if p:
            print(p.val)
            if p.right != None:
                s.append(p.right)

            p = p.left
        else:
            p = s[-1]
            s.pop()
    return


# 用栈 把中序遍历的非递归方式写出来
def in_order_un_fac(root):
    if root == None:
        return []

    # 非递归的方式就需要用栈 存储右子节点
    s = []
    p = root
    while(p or len(s)):
    # 从根结点开始遍历 先序遍历
        if p:
            s.append(p)
            p = p.left
        else:
            p = s[-1]
            s.pop()
            print(p.val)
            p = p.right
    return


# 用队列完成  广度优先搜索（层次遍历）
def level_order_un_fac(root):
    from queue import Queue
    q = Queue()
    p = root
    if root == None:
        return []
    q.put(p)
    while(p or not q.empty()):
        p = q.get()
        print(p.val)
        if p.left:
            q.put(p.left)
        if p.right:
            q.put(p.right)








if __name__ == "__main__":

    singer = TreeNode("Taylor Swift")

    genre_country = TreeNode("Country")
    genre_pop = TreeNode("Pop")

    album_fearless = TreeNode("Fearless")
    album_red = TreeNode("Red")
    album_1989 = TreeNode("1989")
    album_reputation = TreeNode("Reputation")

    song_ls = TreeNode("Love Story")
    song_wh = TreeNode("White Horse")
    song_wanegbt = TreeNode("We Are Never Ever Getting Back Together")
    song_ikywt = TreeNode("I Knew You Were Trouble")
    song_sio = TreeNode("Shake It Off")
    song_bb = TreeNode("Bad Blood")
    song_lwymmd = TreeNode("Look What You Made Me Do")
    song_g = TreeNode("Gorgeous")

    singer.left, singer.right = genre_country, genre_pop
    genre_country.left, genre_country.right = album_fearless, album_red
    genre_pop.left, genre_pop.right = album_1989, album_reputation
    album_fearless.left, album_fearless.right = song_ls, song_wh
    album_red.left, album_red.right = song_wanegbt, song_ikywt
    album_1989.left, album_1989.right = song_sio, song_bb
    album_reputation.left, album_reputation.right = song_lwymmd, song_g

    print(list(pre_order(singer)))
    print(list(in_order(singer)))
    print(list(post_order(singer)))
    level_order_un_fac(singer)
