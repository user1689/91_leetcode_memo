## 题目
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

## 思路
哈希表+滑动窗口，哈希集合+滑动窗口

## python
```python3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 写法一 哈希表+滑动窗口
        # time n
        # space n
        # slidng window + hashMap
        curlen = 0
        maxlen = 0
        # 定义左右指针
        start, end = 0, 0
        hashMap = {}
        while end < len(s):
            # 获取当前字符
            char = s[end]
            # corner case: "abba"
            # 如果当前字符存在于哈希表并且hashMap[char](上次出现的idx)大于等于start
            # 说明此时出现了重复字符 需要将start指向上一次出现重复字符的idx+1位置
            if char in hashMap and hashMap[char] >= start:
                start = hashMap[char] + 1

            # 更新哈希表中最后一次出现char为end的位置
            hashMap[char] = end
            # 计算长度
            curlen = end - start + 1
            maxlen = max(curlen, maxlen)
            end += 1
        return maxlen

# eg: "abca"
# 当start = 0, end = 3 
# {a:0, b:1, c:2} 代表字符a最后出现于idx0位置...,b...,c...
# 此时s[end]存在于哈希表中
# 先更新start = hashMap[s[end]] + 1 即 start = 1
# 再更新哈希表中s[end]字符最后一次出现的位置 即{a:3, b:1, c:2}

# 参考题解
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/python-zhu-bu-you-hua-cong-bao-li-fa-dao-6i34/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 写法二 哈希集合+滑动窗口
        # time n
        # space n
        # 滑动窗口
        
        memo = set()
        left = 0
        max_len = 0
        cur_len = 0
        for i in range(0, len(s)):
            cur_len += 1
            # 发现重复
            # 从集合中移出, 移动left, 减少当前长度
            # 一直移动左边界直到s[i]不在memo中，因为有可能字符不在边界上
            # corner case:
            # "pwwkew"
            while s[i] in memo:
                memo.remove(s[left])
                left += 1
                cur_len -= 1

            if cur_len > max_len: 
                max_len = cur_len
            # 不重复就加入等待下次判断
            memo.add(s[i])
        return max_len
```
## 复杂度分析
* time n
* space n

## 相关题目
1. https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-by-powcai/
2. https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/yi-ge-mo-ban-miao-sha-10dao-zhong-deng-n-sb0x/
