class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root: return None
        queue = deque([root])
        op = []
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                level.append(node.val)
            op.append(sum(level)/len(level))
        return op
        
