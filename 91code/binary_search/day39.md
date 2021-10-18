## 题目
https://binarysearch.com/problems/Triple-Inversion

## 思路
binarySearch, mergeSort

## python3
```python3
import bisect
class Solution:
    # 思路一
    # 二分
    def solve(self, nums):
        ans = 0
        tmp = []
        for a in nums:
            i = bisect.bisect_right(tmp, a * 3)
            ans += len(tmp) - i
            bisect.insort_right(tmp, a)
        return ans

class Solution:
    def solve(self, nums):
        
        # time nlogn
        # space n
        # mergeSort
        self.count = 0

        def divide(low, high):
            if (low < high):
                mid = low + (high - low) // 2
                divide(low, mid)
                divide(mid + 1, high)
                merge(low, mid, high)
        
        def merge(low, mid, high):
 
            tmp = []
            i, j = low, mid + 1
            while i <= mid and j <= high:
                if (nums[i] <= nums[j]):
                    tmp.append(nums[i])
                    i += 1
                elif (nums[i] > nums[j]):
                    tmp.append(nums[j])
                    j += 1

            # 归并排序保证了一定有ti < tj
            # eg: 
            # ti    tj
            # [1,7] [2,5]
            # 1和2对比 ti+=1 (当1<3*2说明得在1当中继续找更得数看看会不会大于3*2，所以ti往后移)
            # 7和2对比 tj+=1 (7>3*2 计数器+1 然后tj往后移看是否还存在7>3*nums[tj]的情况)
            # 7和5对比 ti+=1 (7<3*5 7为左边数组最大的元素了，如果它都不大于3*nums[tj]，就不可能再有更大的了，所以退出循环，计数完成)

            ti, tj = low, mid + 1
            while ti <= mid and tj <= high:
                if (nums[ti] <= (3 * nums[tj])):
                    ti += 1
                elif (nums[ti] > (3 * nums[tj])):
                    self.count += mid - ti + 1
                    tj += 1
                
            while (i <= mid):
                tmp.append(nums[i])
                i += 1

            while (j <= high):
                tmp.append(nums[j])
                j += 1

            for i in range(0, len(tmp)):
                nums[low] = tmp[i]
                low += 1

        divide(0, len(nums) - 1)  
        return self.count  
```

## 时间复杂度
* time nlogn
* space n

## 相关题目
1.https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
