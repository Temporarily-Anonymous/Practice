class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None or root.right == None:
            return self.minDepth(root.left) + self.minDepth(root.right) + 1
        return min(self.minDepth(root.right), self.minDepth(root.left)) + 1



root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
Demo = Solution()
result = Demo.minDepth(root)
print(result)
