# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, root, sub):
        if not root and not sub:
            return True
        if(root and sub and root.val == sub.val):
            return self.isSameTree(root.left, sub.left) and self.isSameTree(root.right, sub.right)

        return False
