import enum
import collections
from dataclasses import dataclass
from typing import List

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
    def is_valid_position(self, pos: Position, rooms: List[List[str]]) -> bool:
        return (
            pos.x >= 0 and
            pos.y >= 0 and
            pos.x < len(rooms) and
            pos.y < len(rooms[0])
        )


    def walls_and_gates(self, rooms: List[List[int]]):
        queue = collections.deque()
        
        num_rows = len(rooms)
        num_cols = len(rooms[0])

        for i in range(num_rows):
            for j in range(num_cols):
                if rooms[i][j] == 0:
                    gate_pos = Position(i, j)
                    queue.append(gate_pos)
        
        while queue:
            curr_pos = queue.popleft()
            curr_val = rooms[curr_pos.x][curr_pos.y]
            for direction in Directions:
                new_pos = curr_pos + direction.value

                if self.is_valid_position(
                    new_pos,
                    rooms
                ):
                    new_val = rooms[new_pos.x][new_pos.y]

                    if new_val > curr_val + 1:
                        rooms[new_pos.x][new_pos.y] = curr_val + 1
                        queue.append(new_pos)
