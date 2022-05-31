## 题目
https://www.geeksforgeeks.org/find-the-length-of-the-longest-subarray-with-atmost-k-occurrences-of-the-integer-x/

## python3
```python3
class solution:
    def longest(self, arr, k):
        left = 0
        right = 0
        n = len(arr)
        ans = 0
        
        while (right < n):
            if (arr[right] == 0):
                k -= 1
            while (k < 0):
                if (arr[left] == 0):
                    k += 1
                left += 1
            if (right - left + 1 > ans):
                maxL = left
                ans = right - left + 1
            right += 1
        
        res = []
        for i in range(0, ans):
            if (arr[maxL + i] == 0):
                res.append(maxL + i)
        return res
        
obj = solution()
a = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,0,0,0,0]
obj.main(a, 3)
```
