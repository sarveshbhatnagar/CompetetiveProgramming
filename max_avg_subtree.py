from cmath import inf


class TreeNode:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    node_avg = dict()

    def max_avg(self, root):
        if root.children == [] or not root.children:
            # self.node_avg[root.val] = root.val
            return root.val, 1

        mavg = 0
        count = 0
        for child in root.children:
            mavg += self.max_avg(child)[0]
            count += self.max_avg(child)[1]

        self.node_avg[root.val] = (mavg+root.val)/(count+1)
        return self.node_avg[root.val], count + 1

    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.max_avg(root)

        mval = -inf
        snode = None
        for i in self.node_avg:
            if self.node_avg[i] > mval:
                mval = self.node_avg[i]
                snode = i

        return mval, snode


n4 = TreeNode(11, [])
n5 = TreeNode(2, [])
n6 = TreeNode(3, [])
n7 = TreeNode(15, [])
n8 = TreeNode(8, [])
n2 = TreeNode(12, [n4, n5, n6])
n3 = TreeNode(18, [n7, n8])
n1 = TreeNode(20, [n2, n3])

print(Solution().maximumAverageSubtree(n1))
