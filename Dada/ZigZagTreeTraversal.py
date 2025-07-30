# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections
from typing import List, NamedTuple, Optional

class TraversalNode(NamedTuple):
    depth: int
    node: TreeNode

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = collections.deque()
        traversals = collections.defaultdict(list)
        
        queue.append(
            TraversalNode(0, root)
        )

        while queue:
            curr = queue.pop()
            depth = curr.depth
            node = curr.node

            traversals[depth].append(
                node.val
            )

            new_depth = depth + 1
            children = [node.left, node.right]

            for child in children:
                if child:
                    queue.append(
                        TraversalNode(new_depth, child)
                    )
            
        res = {}

        for depth, nodes in traversals.items():
            new_nodes = nodes

            if depth % 2 == 0:
                new_nodes = list(reversed(new_nodes))
            
            res[depth] = new_nodes
        
        return list(res.values())
