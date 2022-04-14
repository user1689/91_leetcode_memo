## 题目
https://leetcode-cn.com/problems/trapping-rain-water/

## 思路

## python3
```python3
class Solution:
    def trap(self, height: List[int]) -> int:

        '''
        dp加速
        [4,2,0,3,2,5]
        
          <-
        [4,4,4,4,4,5]

          ->
        [5,5,5,5,5,5]
        
        '''
        n = len(height)
        dp1 = [0] * n
        dp2 = [0] * n
        ans = 0
        dp1[0] = height[0]
        dp2[n - 1] = height[n - 1]
        for i in range(1, n):
            dp1[i] = max(dp1[i - 1], height[i])
        for j in range(n-2, -1, -1):
            dp2[j] = max(dp2[j + 1], height[j])
        for i in range(0, n):
            ans += min(dp1[i], dp2[i]) - height[i]
        return ans
        
        
        '''
        stack加速
         0 1 2 3 4 5 6 7 8 9 1011 
        [0,1,0,2,1,0,1,3,2,1,2,1]
        
        [1,2,3]
        i = 1
        left = 0
        bottom = 0
        ww = 1 - 0 - 1
        hh = 0 - 0
        ans += 0


        维护单调递减栈
        遍历获取区间极值

        '''
        stack = []
        ans = 0
        for i in range(0, len(height)):
            
            while (stack and height[stack[-1]] < height[i]):
                # corner case:
                '''       
                height = [0,1,0,2] 当站内只有一个元素时触发了出栈则再弹出bottom_idx停止循环避免报错
                          _
                      _  | |
                    _| |_| |
                '''
                # 当stack内有两个元素 先弹出一个作为bottom 再看栈顶的作为left 如果没有left说明无法接水 退出循环
                # 如果栈顶有left并且高度大于bottom的 说明可以接水 算出i和left的距离*(两个边框值较小的一个和bottom的高度差) 累加到ans
                # 如果有left但是高度等于bottom 此时会被乘法计算中 宽度*0 直接忽略掉
                bottom_idx = stack.pop()
                if (not stack):
                    break
                left_idx = stack[-1]
                ww = i - left_idx - 1
                hh = min(height[i], height[left_idx]) - height[bottom_idx]
                ans += (ww * hh)

            stack.append(i)

        return ans


'''
bruteforce
'''
i = 1
        n = len(height)
        res = 0
        while (i < n - 1):
            j = i
            k = i
            left_max = 0
            while(j >= 0):
                left_max = max(left_max, height[j])
                j -= 1
            right_max = 0
            while(k < n):
                right_max = max(right_max, height[k])
                k += 1
            res += min(left_max, right_max) - height[i]
            i += 1
        return res

```

时间复杂度
* time O(N)
* space O(N)

相关题目
1. 待补充
