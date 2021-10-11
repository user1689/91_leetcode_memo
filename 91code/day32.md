## 题目
https://leetcode-cn.com/problems/robot-return-to-origin/

## 思路
模拟

## python3
```python3
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # time |s|
        # space 1
        # imitation
        # 写法一

        startPos = [0, 0]
        for direct in moves:
            if direct == 'U':
                startPos[1] += 1
            elif direct == 'D':
                startPos[1] -= 1
            elif direct == 'L':
                startPos[0] -= 1
            elif direct == 'R':
                startPos[0] += 1
        
        if (startPos[0] == 0) and (startPos[1] == 0):
            return True
        else:
            return False
            
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # 写法二
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')       
```

## 复杂度分析
* time n
* space 1

## 相关题目
1. https://leetcode-cn.com/problems/number-of-provinces/
