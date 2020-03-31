# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 首先需要明确一点 就是该直径 可能不路过根节点
        # 所以求最大值的时候 每次递归都需要有个比较的过程
        def get_max_deep(node):
            if node == None:
                return 0
            left_max = get_max_deep(node.left)
            right_max = get_max_deep(node.right)
            # 更新结果
            self.ans = max(self.ans, 1+left_max+right_max)
            return max(left_max, right_max) + 1

        get_max_deep(root)
        return self.ans - 1

