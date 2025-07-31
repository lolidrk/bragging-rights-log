from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbersWithIntermediateStep(
        self,
        root: Optional[TreeNode],
        intermediate: int
    ):
        if root is None:
            return 0
  
        new_intermediate = intermediate * 10 + root.val

        if root.left is None and root.right is None:
            return new_intermediate
        
        left_val = self.sumNumbersWithIntermediateStep(
            root.left,
            new_intermediate
        )
        right_val = self.sumNumbersWithIntermediateStep(
            root.right,
            new_intermediate
        )

        return left_val + right_val
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.sumNumbersWithIntermediateStep(
            root,
            0
        )