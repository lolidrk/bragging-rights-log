from typing import List, Set
class Solution:
    def get_bin_rep(self, num: int) -> Set[int]:
        power = 0
        bin_rep = set()

        while num > 0:
            if num % 2:
                bin_rep.add(power)
            
            power += 1
            num //= 2
        
        return bin_rep

    def longestNiceSubarray(self, nums: List[int]) -> int:
        first_num = nums[0]
        curr_bin_rep = self.get_bin_rep(first_num)
        mem_bin_rep = {first_num: curr_bin_rep.copy()}

        start = 0
        end = 1
        res = 1
        length = len(nums)

        while end < length:
            new_num = nums[end]
            new_num_bin_rep = self.get_bin_rep(new_num)
            mem_bin_rep[new_num] = new_num_bin_rep

            if not (new_num_bin_rep & curr_bin_rep):
                curr_bin_rep |= new_num_bin_rep
            else:
                while start < end:
                    start_num = nums[start]
                    start_num_bin_rep = mem_bin_rep[start_num]

                    curr_bin_rep -= start_num_bin_rep
                    start += 1

                    if not (new_num_bin_rep & curr_bin_rep):
                        curr_bin_rep |= new_num_bin_rep
                        break
            
            res = max(res, end - start + 1)
            end += 1
        
        return res
