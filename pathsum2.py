from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.result = []
        if(not root):
            return self.result

        def dfs(nd, path, curSum):
            if(not nd):
                return
            if(not nd.left and not nd.right):
                if(curSum+nd.val == targetSum):
                    self.result.append(path.copy()+[nd.val])
                return

            dfs(nd.left, path+[nd.val], curSum+nd.val)
            dfs(nd.right, path+[nd.val], curSum+nd.val)

        dfs(root, [], 0)

        return self.result
