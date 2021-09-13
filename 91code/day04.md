## 题目
https://leetcode-cn.com/problems/decode-string/

## 思路
模拟

## python3
```python
# 写法一
class Solution:
    def decodeString(self, s: str) -> str:

        # time s + |s|
        # space n
        # 单栈模拟
        stack = []
 
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                
                # 取出字符
                alpha = list()
                while stack and stack[-1].isalpha():
                    alpha.append(stack.pop())
                # 数组 -> string
                tmp = ""
                for i in range(len(alpha) - 1, -1, -1):
                    tmp += str(alpha[i])
                alpha = tmp
                
                # case:
                # s = "3[ab]2[bc]"
                # stack = ['3','[','a','b']
                # alpha = ['b','a']
                # tmp = "ab"
                
                # 取出[
                if stack and stack[-1] == '[':
                    stack.pop()

                # 取出倍数
                multiple = list()
                while stack and stack[-1].isdigit():
                    multiple.append(stack.pop())
                # 数组 -> string -> int
                tmp = ""
                for i in range(len(multiple) - 1, -1, -1):
                    tmp += str(multiple[i])
                multiple = int(tmp)
                    
                # 放回 倍数个字符
                while multiple > 0:
                    stack.append(alpha)
                    multiple -= 1

        res = ""
        for i in range(0, len(stack)):
            res += stack[i]
        return res

# 写法二
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        multi = 0

        for c in s:
            if c == '[':
                stack.append([multi, res])
                multi, res = 0, ""
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c) 
            else:
                res += c
        
        return res
```

## 时间复杂度
* time s + |s|
* space n

## 相关题目
1 待补充
