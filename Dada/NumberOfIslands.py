import enum
from typing import List, Set
from dataclasses import dataclass

@dataclass(frozen=True)
class Position():
    x: int
    y: int

    def __add__(self, other: "Position"):
        return Position(
            self.x + other.x,
            self.y + other.y
        )

class Directions(enum.Enum):
    UP = Position(0, 1)
    DOWN = Position(0, -1)
    LEFT = Position(1, 0)
    RIGHT = Position(-1, 0)


class Solution:
    def is_valid_position(self, pos: Position, grid: List[List[str]]) -> bool:
        return (
            pos.x >= 0 and
            pos.y >= 0 and
            pos.x < len(grid) and
            pos.y < len(grid[0]) and
            grid[pos.x][pos.y] == "1"
        )

    def traverse(self, curr_pos: Position, grid: List[List[str]], visited: Set[Position]):
        visited.add(curr_pos)

        for direction in Directions:
            new_pos = curr_pos + direction.value

            if (
                self.is_valid_position(
                    new_pos,
                    grid
                ) 
                and not new_pos in visited
            ):
                self.traverse(
                    new_pos,
                    grid,
                    visited
                ) 

    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        visited = set()
        num_rows = len(grid)
        num_cols = len(grid[0])

        for i in range(num_rows):
            for j in range(num_cols):
                curr_pos = Position(i, j)

                if (
                    self.is_valid_position(
                        curr_pos,
                        grid
                    ) 
                    and not curr_pos in visited
                ):
                    num_islands += 1
                    self.traverse(
                        curr_pos,
                        grid,
                        visited
                    )
        
        return num_islands
