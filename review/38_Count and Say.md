## 题目
https://leetcode-cn.com/problems/count-and-say/

## 思路
imitation

## python3
```python3
class Solution:
    def countAndSay(self, n: int) -> str:
    
        def getNext(s):
            length = len(s)
            tmp = ''
            # get head
            head = s[0]
            # set default num
            num = 1
            # count the freq of head
            for i in range(1, length):
                if (s[i] == head):
                    num += 1
                else:
                    # update tmp
                    tmp = tmp + str(num) + str(head)
                    # update head
                    head = s[i]
                    # refresh num
                    num = 1
            s = tmp + str(num) + str(head)
            return s

        s = '1'
        # iterate n times
        for i in range(2, n+1):
            s = getNext(s)
        return s    
```

## 复杂度分析
* time n
* space 1

## 相关题目
1、待补充
