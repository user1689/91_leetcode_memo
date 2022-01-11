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

class Solution:
    def countAndSay(self, n: int) -> str:
        # time n * m
        # space 1
        # twoPointers
        last = "1"
        # iterate n - 1 times
        for _ in range(n - 1):
            tmp = ""
            i = 0
            # iterate begin
            while(i < len(last)):
                start = i
                j = i + 1
                while (j < len(last) and last[start] == last[j]):
                    j += 1
                finish = j - 1
                num = finish - start + 1
                tmp += str(num)
                tmp += str(last[start])
                i = j
            last = tmp
        return last
```

## 复杂度分析
* time n * m  (m is the max length of the string programs generate)
* space 1

## 相关题目
1、待补充
