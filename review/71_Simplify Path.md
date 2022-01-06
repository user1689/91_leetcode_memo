## 题目
https://leetcode-cn.com/problems/simplify-path/

## 思路
stack, deque

## python3
```python3
class Solution:
    def simplifyPath(self, path: str) -> str:
        # time n
        # space n
        # 思路
        # 分情况讨论
        # 第一种情况 / or .
        # 第二种情况 ..
        # 第三种情况 字母字符
        tmp = [] 
        splits = path.split('/')
        for char in splits:
            if char == '':
                continue
            if char == '.':
                continue
            if char == '..':
                if len(tmp) != 0:
                    tmp.pop()
            else:
                tmp.append(char)
        # print(''.join(tmp))
        return '/' + '/'.join(tmp)
```

## 复杂度分析
* time n
* space n

## 相关题目
1. 待补充
