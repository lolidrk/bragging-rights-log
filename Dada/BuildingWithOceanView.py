from typing import (
    List, NamedTuple
)

class IndexedHeight(NamedTuple):
    height: int
    index: int

class Solution:
    """
    @param heights: An integer array
    @return: Indexs of buildings with sea view
    """
    def find_buildings(self, heights: List[int]) -> List[int]:
        acceptable_buildings = [
            IndexedHeight(
                heights[0],
                0
            )
        ]

        for i in range(1, len(heights)):
            while (
                acceptable_buildings and 
                acceptable_buildings[-1].height <= heights[i]
            ):
                acceptable_buildings.pop()
            
            acceptable_buildings.append(
                IndexedHeight(
                    heights[i],
                    i
                )
            )

        indices = [
            acceptable_building.index 
            for acceptable_building in acceptable_buildings
        ]

        return indices