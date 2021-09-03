from enum import Enum, auto

class Direction(Enum):
  UP =  auto()
  DOWN = auto()
  LEFT = auto()
  RIGHT = auto()

def move(direction, x, y):
  if direction == Direction.UP:
    return x, y+1
  if direction == Direction.DOWN:
    return x, y-1
  if direction == Direction.LEFT:
    return x-1, y
  if direction == Direction.RIGHT:
    return x+1, y
  raise Exception("Unexpected direction:", direction)

