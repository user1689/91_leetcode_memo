## 题目
https://leetcode-cn.com/problems/shortest-distance-to-a-character/

## 思路
最小数组

## python3
```python
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # 思路一 最小数组
        # 因为最近的c无非在字母的左边或者右边
        # 两次遍历 
        # 第一次从左往右维护prev为c的idx然后求出每个坐标到此prev的距离
        # 第二此从右往左维护prev 与第一次的值作对比 将较小的存入

        ans = []
        # 若它左边没有c字母，则idx减去-inf等于inf，配对后面取min
        prev = float('-inf')
        # 从前往后 看每个单词与它左边离它最近的c的距离是多少
        for idx, char in enumerate(s):
            if char == c:
                prev = idx
            ans.append(idx - prev)
        
        prev = float('inf')
        # 从后往前 看每个单词与它右边离它最近的c的距离是多少
        for idx in range(len(s) - 1,  -1, -1):
            if s[idx] == c:
                prev = idx
            ans[idx] = min(ans[idx], prev - idx)
        return ans
```
## 复杂度分析
* time n n为s长度
* space n

## 相关题目
1.（最短距离类型，待补充）
