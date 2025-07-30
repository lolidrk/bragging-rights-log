from typing import List, NamedTuple

class Interval(NamedTuple):
    start: int
    end: int

class Solution:
    def is_interval_mergeable(self, curr_interval: Interval, new_interval: Interval) -> bool:
        '''
        The function returns true if there is any intersection between the two intervals

        Params:
        curr_interval: The current interval
        new_interval: The new interval that can potentially be merged with the current interval

        Returns:
        True if there is intersection between the two intervals
        '''
        return curr_interval.end >= new_interval.start
    
    def merge_intervals(self, curr_interval: Interval, new_interval: Interval) -> Interval:
        '''
        This function merges two intervals which have overlap.

        Params:
        curr_interval: The current interval
        new_interval: The new interval that can potentially be merged with the current interval

        Returns:
        The merged interval
        '''
        merged_interval = Interval(
            min(
                curr_interval.start,
                new_interval.start
            ),
            max(
                curr_interval.end,
                new_interval.end
            )
        )

        return merged_interval
        
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort by the start of each interval
        sorted_intervals = sorted(intervals, key=lambda interval: interval[0])

        num_intervals = len(intervals)
        curr_interval_index = 0
        res = []

        while curr_interval_index < num_intervals:
            curr_interval = Interval(
                sorted_intervals[curr_interval_index][0],
                sorted_intervals[curr_interval_index][1]
            )

            merged_interval = curr_interval
            next_interval_index = curr_interval_index + 1

            while next_interval_index < num_intervals:
                next_interval = Interval(
                    sorted_intervals[next_interval_index][0],
                    sorted_intervals[next_interval_index][1]
                )

                if not self.is_interval_mergeable(merged_interval, next_interval):
                    break
                
                merged_interval = self.merge_intervals(merged_interval, next_interval)
                next_interval_index += 1

            res.append(
                [merged_interval.start, merged_interval.end]
            )    
            curr_interval_index = next_interval_index
        
        return res