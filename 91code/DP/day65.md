## 题目
https://leetcode-cn.com/problems/unique-binary-search-trees/

## 思路
DP


## python3
```python3
class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i]表示以数字i为根节点的BST有多少种组合
        dp = [0 for _ in range(n+1)]
        # 没有根节点的情况初始化为1中组合
        dp[0] = 1
        # 以i为根节点
        for i in range(1, n + 1):
            for k in range(1, n + 1):
                # 左边有k-1个节点 右边有i-k个节点
                dp[i] += dp[k - 1] * dp[i - k]
        return dp[n]

# 1 2 3 4 5
# 

#          k
#  k - 1       n - k
```

## 复杂度分析
* time n**2
* space n

## 相关题目
1. https://leetcode-cn.com/problems/unique-binary-search-trees-ii/
