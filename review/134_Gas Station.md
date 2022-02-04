## 题目
https://leetcode-cn.com/problems/gas-station/

## 思路
imitation

## python3
```python3
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        难点在写出O(n)的算法
        假设[i...j...k] i无法到k并且在j停下 需要证明 在位置 i 和位置 k 之间的所有位置，都不可能是一个合法起点
        在j停下说明, gas[j] = 0
        设从j到k的净消耗为 = x, gas[j] < abs(x)
        所以从j就不能到达k
        '''
        n = len(gas)
        i = 0
        while (i < n):
            j = i
            remains = gas[j]
            # 开始前进
            while (remains - cost[j] >= 0):
                remains = remains - cost[j] + gas[(j + 1) % n]
                j = (j + 1) % n
                if (j == i):
                    return i
            # 加速 
            # 如果绕了一圈都到不了 后面就不用看了 因为已经试过了 
            if (j < i):
                return -1
            # 加速
            i = j
            i += 1
        return -1
        
# proof reference https://leetcode-cn.com/problems/gas-station/solution/gong-shui-san-xie-noxiang-xin-ke-xue-xi-zsgqp/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # time n**2
        # space 1

        # 暴力模拟
        n = len(cost)
        for i in range(0, n):
            j = i
            remains = gas[i]
            # 去下一个点要花费本idx的cost
            while remains - cost[j] >= 0:
                # 到达下个点花费本idx的cost 并获取下一个idx点的gas
                remains = remains - cost[j] + gas[(j + 1) % n]
                # 已经到达下一个点 更新idx
                j = (j + 1) % n
                # 绕了一圈
                if j == i:
                    return i
        return -1
```

## 复杂度分析
* time n
* space 1

## 相关题目
1. 待补充
