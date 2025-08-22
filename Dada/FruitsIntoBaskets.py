from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        unique_fruits = {fruits[0]: 1}
        start = 0
        end = 0
        res = 1

        num_trees = len(fruits)
        num_baskets = 2
        
        while end < num_trees:
            end += 1

            if end >= num_trees:
                break

            new_fruit = fruits[end]
            
            if new_fruit in unique_fruits:
                unique_fruits[new_fruit] += 1
            elif len(unique_fruits) < num_baskets:
                unique_fruits[new_fruit] = 1
            else:
                while start < end:
                    old_fruit = fruits[start]
                    unique_fruits[old_fruit] -= 1
                    start += 1

                    if unique_fruits[old_fruit] == 0:
                        del unique_fruits[old_fruit]
                        unique_fruits[new_fruit] = 1
                        break
            
            res = max(
                res,
                sum(unique_fruits.values())
            )
        
        return res
