class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinarySearchTree:
    def creat_tree(self, array):
        tree_root = TreeNode(array[0])
        def find_position(tree_node, num):
            if num < tree_node.val:
                if tree_node.left is not None:
                    find_position(tree_node.left, num)
                else:
                    tree_node.left = TreeNode(num)
            else:
                if tree_node.right is not None:
                    find_position(tree_node.right, num)
                else:
                    tree_node.right = TreeNode(num)
        for i in array[1:]:
            find_position(tree_root, i)
        return tree_root

    def show_tree(self, tree_root, array):
        tree = {}
        def put_tree_in_list(tree_node):
            tree[tree_node.val] = []
            if tree_node.left:
                tree[tree_node.val].append(tree_node.left.val)
                put_tree_in_list(tree_node.left)
            else:
                tree[tree_node.val].append("NULL")
            if tree_node.right:
                tree[tree_node.val].append(tree_node.right.val)
                put_tree_in_list(tree_node.right)
            else:
                tree[tree_node.val].append("NULL")
        put_tree_in_list(tree_root)
        for node in tree.items():
            print(node)

    def tree_search(self, tree_node, key):
        if tree_node:
            if key == tree_node.val:
                return tree_node
            elif key < tree_node.val:
                return self.tree_search(tree_node.left, key)
            else:
                return self.tree_search(tree_node.right, key)
        else:
            return False

    def tree_minimum(self, tree_root):
        while tree_root.left:
            tree_root = tree_root.left
        return tree_root

    def tree_macximum(self, tree_root):
        while tree_root.right:
            tree_root = tree_root.right
        return tree_root

    def tree_successor(self, tree_root, key):
        temp = [0]
        result = [0]
        def find_tree_successor(tree_node):
            if tree_node:
                find_tree_successor(tree_node.left)
                if temp[0] == key:
                    result[0] = tree_node.val
                    temp[0] = tree_node.val
                else:
                    temp[0] = tree_node.val
                find_tree_successor(tree_node.right)
        find_tree_successor(tree_root)
        return result[0]

    def tree_insert(self, tree_root, key):
        if key < tree_root.val:
            if tree_root.left:
                self.tree_insert(tree_root.left, key)
            else:
                tree_root.left = TreeNode(key)
        else:
            if tree_root.right:
                self.tree_insert(tree_root.right, key)
            else:
                tree_root.right = TreeNode(key)

    def tree_delete(self, tree_root, key):
        if key == tree_root.val:
            if tree_root.left is None and tree_root.right is None:
                tree_root = None
            elif tree_root.left is None:
                tree_root.left = tree_root.right.left
                tree_root.right = tree_root.right.right
            elif tree_root.right is None:
                tree_root.right = tree_root.left.right
                tree_root.left = tree_root.left.left
            else:
                substitute_lastnode = tree_root
                while substitute_lastnode.left.left:
                    substitute_lastnode = substitute_lastnode.left
                substitute_node = substitute_lastnode.left
                substitute_lastnode.left = substitute_node.right
                substitute_node.left = tree_root.left
                substitute_node.right = tree_root.right
        elif key < tree_root.val:
            if tree_root.left:
                self.tree_insert(tree_root.left, key)
        else:
            if tree_root.right:
                self.tree_insert(tree_root.right, key)

array = [15,18,6,17,3,7,13,9,4,20,2]
Demone = BinarySearchTree()
tree_root = Demone.creat_tree(array)
Demone.tree_delete(tree_root, 7)
Demone.show_tree(tree_root, array)
