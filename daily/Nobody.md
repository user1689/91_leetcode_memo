# 二分分类

1. 二分答案
```python3
def binarySearch(nums, target):
    # 左右都闭合的区间 [l, r]
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) >> 1
        if nums[mid] == target: return mid
        # 搜索区间变为 [mid+1, right]
        if nums[mid] < target: l = mid + 1
        # 搜索区间变为 [left, mid - 1]
        if nums[mid] > target: r = mid - 1
    return -1
```

2. 二分寻找最左边的满足条件的值（存在target的情况下二分左界）
```python3
def binarySearch(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) >> 1
        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1
    return l
```

3. 二分寻找最右边的满足条件的值 (存在target的情况下二分右界)
```python3
def binarySearch(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r + 1) >> 1
        if nums[mid] <= target:
            l = mid 
        else:
            r = mid - 1
    return l
```

4. 二分寻找最左插入位置
```python3
def bisect_left(nums, x):
    # 内置 api
    bisect.bisect_left(nums, x)
    # 手写
    l, r = 0, len(A) - 1
    while l <= r:
        mid = (l + r) // 2
        if A[mid] >= x: 
            r = mid - 1
        else: 
            l = mid + 1
    return l
```

5. 二分寻找最右插入位置
```python3
def bisect_right(nums, x):
    # 内置 api
    bisect.bisect_right(nums, x)
    # 手写
    l, r = 0, len(A) - 1
    while l <= r:
        mid = (l + r) // 2
        if A[mid] <= x: 
            l = mid + 1
        else: 
            r = mid - 1
    return l
```


