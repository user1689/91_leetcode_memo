## 题目
https://leetcode-cn.com/problems/add-to-array-form-of-integer/

## 思路

## 代码
```python
# 写法一
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        # 将k转化成数组
        num2 = []
        strK = str(k)
        for element in strK:
            num2.append(element)
        
        # 直接相加 
        res = []
        addCarry = 0
        i, j = len(num) - 1, len(num2) - 1
        while i >= 0 and j >= 0:
            sum_ = num[i] + int(num2[j]) + addCarry
            digit = sum_ % 10
            addCarry = sum_ // 10
            res.append(digit)
            i -= 1
            j -= 1

        # 如果多出digit另外处理
        while i >= 0:
            sum_ = num[i] + addCarry
            digit = sum_ % 10
            addCarry = sum_ // 10
            res.append(digit)
            i -= 1
        
        # 如果多出digit另外处理
        while j >= 0:
            sum_ = int(num2[j]) + addCarry
            digit = sum_ % 10
            addCarry = sum_ // 10
            res.append(digit)
            j -= 1

        # 如果有进位 则加1
        if addCarry:
            res.append(1)
        
        # 因为append的原因，最后得反转
        return res[::-1]

# 写法二 
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # time max(n, logk)
        # space n

        # 写法二
        n = len(num)
        res = collections.deque()
        addCarry = 0
        for i in range(n - 1, -1, -1):
            # 获取k的个位数字求和
            sum_ = num[i] + (k % 10) + addCarry
            # 每次加完k，就去除k的个位
            k //= 10
            # 获取个位
            digit = sum_ % 10
            # 去除个位
            addCarry = sum_ // 10
            res.appendleft(digit)

        # 检查k和addCarry 其中有一个还存在就还得继续计算
        while k > 0 or addCarry > 0:
            sum_ = (k % 10) + addCarry
            k //= 10
            digit = sum_ % 10
            addCarry = sum_ // 10
            res.appendleft(digit)
        
        return list(res)
```


## 复杂度分析
* time max(n, logk)
* space n

## 相关题目
1. https://leetcode-cn.com/problems/plus-one/
2. https://leetcode-cn.com/problems/add-binary/
3. https://leetcode-cn.com/problems/add-strings/
4. https://leetcode-cn.com/problems/add-two-numbers/
5. https://leetcode-cn.com/problems/add-two-numbers-ii/
