# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        result = [[] for i in range(n + 1)]
        result[0].append(None)
        def tree_plus_num(tree, num):
            if tree is not None:
                tree.val += num
                tree_plus_num(tree.left, num)
                tree_plus_num(tree.right, num)

        for i in range(1, n + 1):
            for j in range(i):
                for left in result[j]:
                    for right in result[i - 1 - j]:
                        tree = TreeNode(j + 1)
                        tree.left = left
                        tree.right = right
                        result[i].append(tree)
        return result[n]

Demo = Solution()
result = Demo.generateTrees(3)
print(result)