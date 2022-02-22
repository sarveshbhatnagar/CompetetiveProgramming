
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS.
        if(not root):
            return []

        result = [root]
        ans = []
        while len(result) > 0:
            newResult = []
            newAns = []
            for res in result:
                newAns.append(res.val)
                if(res.left):
                    newResult.append(res.left)
                if(res.right):
                    newResult.append(res.right)
            ans.append(newAns)
            result = newResult

        return ans
