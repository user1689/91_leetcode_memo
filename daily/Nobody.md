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
    
def binarySearchLeft(nums, target):
    # 左右都闭合的区间 [l, r]
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) >> 1
        if nums[mid] == target:
            # 收缩右边界
            r = mid - 1;
        # 搜索区间变为 [mid+1, right]
        if nums[mid] < target: l = mid + 1
        # 搜索区间变为 [left, mid - 1]
        if nums[mid] > target: r = mid - 1
    if l >= len(nums) or nums[l] != target: return -1
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
    
def binarySearchRight(nums, target):
    # 左右都闭合的区间 [l, r]
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) >> 1
        if nums[mid] == target:
            # 收缩左边界
            l = mid + 1;
        # 搜索区间变为 [mid+1, right]
        if nums[mid] < target: l = mid + 1
        # 搜索区间变为 [left, mid - 1]
        if nums[mid] > target: r = mid - 1
    if r < 0 or nums[r] != target: return -1
    return r
```

4. 二分寻找最左插入位置
```python3
def bisect_left(nums, x):
    # 内置 api
    bisect.bisect_left(nums, x)
    # 手写
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] >= x: 
            r = mid - 1
        else: 
            l = mid + 1
    return l
# eg: nums = [1,2,5,8], target = 5
# --> 2
```

5. 二分寻找最右插入位置
```python3
def bisect_right(nums, x):
    # 内置 api
    bisect.bisect_right(nums, x)
    # 手写
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] <= x: 
            l = mid + 1
        else: 
            r = mid - 1
    return l
# eg: nums = [1,2,5,8], target = 5
# --> 3
```

# 滑动窗口

# DFS
1. permutations
```python3
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        depth, path, res = 0, [], []
        ls_used = [False for _ in nums]

        self.dfs(nums, depth, ls_used, path, res)
        return res
    
    def dfs(self, nums, depth, ls_used, path, res):
        # base
        if depth == len(nums):
            res.append(path[:])
            return
        # 
        for (i, used) in enumerate(ls_used):
            if used:
                continue
            path.append(nums[i])
            ls_used[i] = True
            self.dfs(nums, depth + 1, ls_used, path, res)
            path.pop()
            ls_used[i] = False

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        res = []
        path = []

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack(path)
                path.pop()
        
        backtrack(path)
        return res

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        res = []

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path)
                return
            for num in nums:
                if num in path:
                    continue
                backtrack(path + [num])
        
        backtrack([])
        return res
```
2. permutations ii
```python3
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # time n * n!
        # space n
        # permutationUnique
        def dfs(path):
            if len(path) == len(nums):
                res.append(path)
            
            for i in range(0, len(nums)):
                if visited[i]:
                    continue
                '''
                我是这样理解的，for循环保证了从数组中从前往后一个一个取值，再用if判断条件。所以nums[i - 1]一定比nums[i]先被取值和判断。如果nums[i - 1]被取值了，那vis[i - 1]会被置1，只有当递归再回退到这一层时再将它置0。每递归一层都是在寻找数组对应于递归深度位置的值，每一层里用for循环来寻找。所以当vis[i - 1] == 1时，说明nums[i - 1]和nums[i]分别属于两层递归中，也就是我们要用这两个数分别放在数组的两个位置，这时不需要去重。但是当vis[i - 1] == 0时，说明nums[i - 1]和nums[i]属于同一层递归中（只是for循环进入下一层循环），也就是我们要用这两个数放在数组中的同一个位置上，这就是我们要去重的情况。
                '''
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                
                visited[i] = True
                dfs(path + [nums[i]])
                visited[i] = False

        # 保证所有一样的数字在一起，这样才能够进行剪枝
        nums.sort()
        visited = [False] * len(nums)
        res = []
        path = []  
        dfs(path)
        return res

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, path = [], []
        used = [False] * len(nums)
        
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(0, len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i -1] and not used[i -1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack(path)
        return res

```
3. combinations
```python3
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(startnum, path):
            if len(path) == k:
                res.append(path[:])
            for num in range(startnum, n + 1):
                path.append(num)
                backtrack(num + 1, path)
                path.pop()

        backtrack(1, path)
        return res
       
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        # time ? (Cnk * k)
        # space ? (k)
        def dfs(startNum, path, k):
            # 剪枝
            # 当前可以选择的数量 < 还需要选择的数量
            if n - startNum + 1 < (k - len(path)):
                return 
            
            if len(path) == k:
                res.append(path)
                return
                
            for num in range(startNum, n+1):
                dfs(num + 1, path + [num], k)

        res = []
        dfs(1, [], k)
        return res
            
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # time ? (Cnk * k)
        # space ? (k)
        # 类二进制枚举写法
        def dfs(startNum, path, k):
            # 剪枝
            # 当前可以选择的数量 < 还需要选择的数量
            if n - startNum + 1 < (k - len(path)):
                return

            if 0 == k:
                res.append(path[:])
                return

            if startNum == n + 1:
                return
            
            dfs(startNum + 1, path, k)
            
            path.append(startNum)
            dfs(startNum + 1, path, k - 1)
            path.pop()

        # time ? (Cnk * k)
        # space ? (k)
        # def dfs(startNum, path, k):
        #     # 剪枝
        #     # 当前可以选择的数量 < 还需要选择的数量
        #     if n - startNum + 1 < (k - len(path)):
        #         return 
        #     if len(path) == k:
        #         res.append(path[:])
        #     for num in range(startNum, n+1):
        #         path.append(num)
        #         dfs(num + 1, path, k)
        #         path.pop()

        res = []
        dfs(1, [], k)
        return res

```
4. combination sum
```python3
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        # tmp = 0
        sum = 0

        def backtrcak(startIdx, sum):
            # if len(path) == len(candidates):
            #     return
            if sum > target:
                return
            if sum == target:
                res.append(path[:])
                return
                
            for i in range(startIdx, len(candidates)):
            # for num in candidates:
                sum += candidates[i]
                path.append(candidates[i])
                backtrcak(i, sum)
                path.pop()
                sum -= candidates[i]
        
        backtrcak(0, sum)
        return res
        
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        # tmp = 0

        def backtrcak(startIdx, remains):
            # if len(path) == len(candidates):
            #     return
            if remains < 0:
                return
            if remains == 0:
                res.append(path[:])
                return
                
            for i in range(startIdx, len(candidates)):
            # for num in candidates:
                # tmp += candidates[i]
                path.append(candidates[i])
                backtrcak(i, remains - candidates[i])
                path.pop()
                # tmp -= candidates[i]
        
        backtrcak(0, target)
        return res

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(startIdx, path, total):
            if total > target:
                return
            
            if total == target:
                res.append(path)
                return
            
            for i in range(startIdx, len(candidates)):
                # visited.add(candidates[i])
                dfs(i, path + [candidates[i]], total + candidates[i])
                
        res = []
        path = []
        dfs(0, path, 0)
        
        return res
            
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # time n * 2**n
        # space target
        # 二进制枚举
        def dfs(idx, path, total):
            if total > target:
                return
            # 顺序有差别的 这么写当idx==len（candidates）时也可以加入
            if total == target:
                res.append(path[:])
                return

            if idx == len(candidates):
                return 

            # 不选
            dfs(idx + 1, path, total)

            # 选
            if candidates[idx] <= target - total:
                path.append(candidates[idx])
                dfs(idx, path, total + candidates[idx])
                path.pop()
                
        res = []
        path = []
        dfs(0, path, 0)
        
        return res

```
5. combination sum ii
```python3
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def backtrack(startIdx, remains):
            if remains < 0:
                return
            if remains == 0:
                res.append(path[:])
                return 

            for i in range(startIdx, len(candidates)):
                if candidates[i] > remains:
                    break
                if i > startIdx and candidates[i] == candidates[i - 1]:
                    continue
                remains -= candidates[i]
                path.append(candidates[i])
                backtrack(i + 1, remains)
                path.pop()
                remains += candidates[i]

        backtrack(0, target)
        return res

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        
        # 问:为什么本题和39还有77不同？为不能用二进制枚举？
        # 答1:此题在candidates上有重复,而39和77都没有重复
        # 答2:因为在39和77中 元素唯一 并且idx的增长从而避免了选择到不同位置的相同元素的可能性,不过勉强点说应该也是可以用,对答案做一个去重即可,但是我写的用数组去重(n**2的复杂度)会超时
        
        def dfs(startIdx, path, total):
            if total > target:
                return
            # 第二次错了...
            # 顺序有差别的 这么写当idx==len（candidates）时也可以加入
            # 因为一般来说最初的传入都是startidx都是0 
            # 所以当idx==1时候其实才刚选了nums[0] 所以当idx==n的时候才刚选了nums[n-1] 是可以加入答案的
            if total == target:
                res.append(path)
                return

            if startIdx == len(candidates):
                return
            

            for i in range(startIdx, len(candidates)):
                if (i > startIdx) and (candidates[i - 1] == candidates[i]):
                    continue
                dfs(i + 1, path + [candidates[i]], total + candidates[i])

        candidates.sort()
        res = []
        dfs(0, [], 0)
        return res
        
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # time (2**n) * m (n为candidates长度, m 为 freq长度)
        # space n
        # 二进制枚举 + freq(hashTable)

        def dfs(idx, rest):
            nonlocal sequence
            if (rest == 0):
                ans.append(sequence[:])
                return

            if (idx == len(freq)) or (freq[idx][0] > rest):
                return
            
            # 开始决定选还是不选

            # 不选当前数
            dfs(idx+1, rest)

            # 选当前数
            # 计算最多可以选几个
            most = min(rest // freq[idx][0], freq[idx][1])
            for i in range(1, most+1):
                sequence.append(freq[idx][0])
                dfs(idx+1, rest - (i * freq[idx][0]))
            sequence = sequence[:-most]

        tmp = collections.Counter(candidates)
        freq = sorted(tmp.items())
        ans = list()
        sequence = list()
        dfs(0, target)
        return ans

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # time (2**n) * m (n为candidates长度, m 为 freq长度)
        # space n
        # 二进制枚举 + freq(hashTable)

        def dfs(idx, rest, sequence):
            # nonlocal sequence
            if (rest == 0):
                ans.append(sequence)
                return

            if (idx == len(freq)) or (freq[idx][0] > rest):
                return
            
            # 开始决定选还是不选

            # 不选当前数
            dfs(idx+1, rest, sequence)

            # 选当前数
            # 计算最多可以选几个
            most = min(rest // freq[idx][0], freq[idx][1])
            for i in range(1, most+1):
                # sequence.append(freq[idx][0])
                dfs(idx+1, rest - (i * freq[idx][0]), sequence + (i * [freq[idx][0]]))
            # sequence = sequence[:-most]

        tmp = collections.Counter(candidates)
        freq = sorted(tmp.items())
        ans = list()
        sequence = list()
        dfs(0, target, sequence)
        return ans
```

# 动态规划

# 基础数据结构
1. 数组

2. 哈希表

3. 链表

4. 双端队列

5. 优先队列/堆
```python3
class heapq:
    def __init__(self, descend = False):
        self.heap = []
        self.descend = descend

    # @property
    def size(self):
        return len(self.heap)
    
    def top(self):
        if self.heap:
            return self.heap[0]
        return None
    
    def push(self, val):
        '''
        存入末尾
        上浮
        '''
        self.heap.append(val)
        self._sift_up(self.size() - 1)
    
    def pop(self):
        '''
        存入tmp
        交换元素
        删除元素
        下沉
        返回tmp
        '''
        tmp = self.top()
        self._swap(0, self.size() - 1)
        self.heap.pop()
        self._sift_down(0)
        return tmp
    

    def _smaller(self, lst, rst):
        return lst > rst if self.descend else lst < rst


    def _swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]


    def _sift_up(self, idx):
        while idx != 0:
            parentIdx = (idx - 1) // 2

            if self._smaller(self.heap[parentIdx], self.heap[idx]):
                break
            
            self._swap(idx, parentIdx)
            idx = parentIdx

    def _sift_down(self, idx):
        while idx*2+1 < self.size():
            smallestIdx = idx
            leftIdx = idx*2+1
            rightIdx = idx*2+2

            if self._smaller(self.heap[leftIdx], self.heap[smallestIdx]):
                smallestIdx = leftIdx
            
            if rightIdx < self.size() and self._smaller(self.heap[rightIdx], self.heap[smallestIdx]):
                smallestIdx = rightIdx
            
            if smallestIdx == idx:
                break

            self._swap(idx, smallestIdx)
            idx = smallestIdx
```

6. 字典树
