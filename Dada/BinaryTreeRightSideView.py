# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections
from typing import NamedTuple

class TraversalNode(NamedTuple):
    depth: int
    node: TreeNode

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root is None:
            return []
        
        root_depth = 0

        queue = collections.deque()
        queue.append(
            TraversalNode(root_depth, root)
        )

        elements = {
            root_depth: root.val
        }

        while queue:
            curr = queue.popleft()
            curr_depth = curr.depth
            curr_node = curr.node

            if curr_depth not in elements:
                elements[curr_depth] = curr_node.val
            
            child_depth = curr_depth + 1
            children = [curr_node.right, curr_node.left]

            for child in children:
                if child:
                    queue.append(
                        TraversalNode(child_depth, child)
                    )

        res = elements.values()    
        return list(res)

