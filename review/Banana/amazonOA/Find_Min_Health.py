from typing import List


class solution:
  def findMinHealth(self, power: List[int], armor: int) -> int:
    # (total damage - prevent damage) + 1 
    return sum(power) - min(max(power), armor) + 1