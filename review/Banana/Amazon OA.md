## Amazon OA



### OA1

#### Nine_Box

- 给一串字符，"abcdefgabc"，然后用自定义的手机九宫格打出。自定义的手机九宫格可以是任何字母组合，唯一要求是每个键至少有两个字母，最多三个字母。换句话说，这里的键位不一定是我们常见的2=abc，3=def等等，可以是1=agq，2=bhj...任何顺序都可以。要求找出能打出输入字符串的最少按键次数。

```python
'''
    frequency
    
    abacadefghibj
    
    tmp = 1-9 ：1   9
         10-18 ：2  9
         19-26 : 3  7
         
    idx = tmp-1
         
    16+7=23
    26-18 = 7 
    
    a:3 ->3*1
    b:2 ->2*1
    c:1
    d:1
    e:1
    f:1
    g:1 
    h:1
    i:1
    	出现次数*按键次数
    j:1  1*2    
'''
class solution:
    def minimumTypingTimes(self, s: str) -> int:
    		map = dict()
        n = len(s)
        for i in range(0, n):
            char = s[i]
            map[char] = map.get(char, 0) + 1
        sorted_tmp = sorted(map.items(), key=lambda x:x[1], reverse=True)
        # print(sorted_tmp)
        ans = 0
        for idx, pair in enumerate(sorted_tmp):
            # print(idx)
            # print(pair)
            if (0 <= idx <= 9):
            		ans += (1 * pair[1])
            elif (10 <= idx <= 18):
        				ans += (2 * pair[1])
            else:
              	ans += (3 * pair[1])
        return ans
      
obj = solution()
test_arr = ["avsczsszz", "abacadefghibj", "hello", "apple"]
res = []
for test in test_arr:
		res.append(obj.minimumTypingTimes(test))
print(res)
```



#### Max_Average_Stock

- 给一个长度为n的数组表示n个月的股价，给定k值，给连续k月并且k个值各不一样的区间求和，找到最大和。例子：｛1，2，3，4｝，k=2，那总共有(1,2) (2,3)(3,4)三个长度为k的连续区间并且每个区间没有重复数值，最大和是7。

```python
class solution:
    def max_average_stock_price(self, arr, k) -> int:
        
        '''
          [1,2, 7, 7, 4, 3, 6]
        [0,1,3,10,17,21,24,30]
           i    j 
        '''
        
        prefix_sum = [0] * (len(arr) + 1) 
        for i in range(0, len(arr)):
            prefix_sum[i+1] = arr[i] + prefix_sum[i]
        i = 0
        j = 0
        n = len(arr)
        seen = set()
        ans = -1
        while(i < n and j < n):
            while(j == n and (j - i > k)):
                i += 1
            
            while((i < n and j < n and arr[j] in seen)):
                seen.remove(arr[i])
                i += 1
                
            # while(j < n and j <= k - 1):
            #     seen.add(arr[j])
            #     j += 1
            
            seen.add(arr[j])
            j += 1
            
            if ((j - i) == k):
                ans = max(ans, prefix_sum[j] - prefix_sum[i])
                if (i < n):
                    seen.remove(arr[i])
                    i += 1
                    
        if (ans != -1):
            tmp = sum(seen)
            ans = max(ans, tmp)    
        
        return ans
    
obj = solution()
arr = [1,2,7,7,4,3,6]
arr2 = [0,0,0,0,0,1]
arr3 = [1,1,1,1,1,1,1,1]
arr4 = [1]
arr5 = []
arr6 = [0]
k = 3
obj.max_average_stock_price(arr, k)
```

#### Find_Data_Locations

- 给了三个list, initinal locations, moveFrom, moveTo, 求从moveFrom 到 moveTo 后， return 各个物品的位置 从小到大

```python
def dataMovement(data, moveFrom, moveTo):
  	s = set(data)
    for destination, origination in zip(moveFrom, moveTo):
      	s.remove(moveFrom)
        s.add(moveTo)
    return sorted(s)
  	# return list(s).sort()

class solution:
    def find_data_locations(self, locations, movedFrom, movedTo):
        map = dict()
        for ll in locations:
            map[ll] = ll
        n = len(movedFrom)
        for i in range(0, n):
            if (movedFrom[i] != movedTo[i]):
                map[movedTo[i]] = movedTo[i]
                del map[movedFrom[i]]
        ans = []
        tmp = sorted(map.items(), key=lambda x: x[1], reverse=False)
        for key, val in tmp:
            ans.append(val)
        return ans
      
obj = solution()
locations = [1,7,6,8]
movedFrom = [1,7,2]
movedTo = [2,9,5]
obj.find_data_locations(locations, movedFrom, movedTo)
```

#### Searchword & Resultword

- 一个searchWord和一个resultWord，问最少给searchWord末尾添加几个字符，可以让resultWord成为它的一个subsequence。举个栗子：search给Word=“armaze”，resultWord=”amazon”，则应该返回2（添加on）。

```python
class solution:
    def searchWordAndResultWord(self, searchWord, resultWord) -> int:
        '''
        "z"
        "acdefg"
        
        "a"
        "acdefg"
        
        "azpxpzle"
        "applepie"
        
        "bgagnsxfadhnfaf"
        "bananapie"
        '''
        i = 0
        j = 0
        n = len(searchWord)
        m = len(resultWord)
        while (i < n and j < m):
            if (searchWord[i] == resultWord[j]):
                i += 1
                j += 1
            i += 1
        return m - j
      
obj = solution()
searchWord = "a"
resultWord = "acdefg"
obj.searchWordAndResultWord(searchWord, resultWord)
```

#### User_System_Design

- 写一个简单的api，有三个功能 register，log in，log out。register的时候要输入name和password，如果这个用户已经register过了要返回username already exists，没有的话返回registered successfully；log in时也要name和password，如果该name并没有register或者已经logged in，或者password错误，要返回log in unsuccessful，如果都满足就返回logged in successfully；最后是log out，也是很直观的逻辑，正常的话返回成功，没有regist‍‌‍‌‍‍‌‌‌‍‍‍‍‍‌‍‌er或者没有log in的name要返回log out失败。

```python
class solution:
    def userSystem(self, operations) -> None:
        map = dict()
        ans = []
        for opt in operations:
            tmp = opt.split(' ')
            action, username = tmp[0], tmp[1]
            password = tmp[2] if len(tmp) == 3 else ""

            if (action == "register"):
                if (username in map.keys()):
                    ans.appned("Registered Unsuccessful")
                else:
                    if (password == ""):
                        ans.append("Registered Unsuccessful")
                    else:
                        map[username] = [password, 0]
                        ans.append("Registered Successfully")
            elif (action == "login"):
                if (username not in map.keys()):
                    ans.append("Login Unsuccessful")
                else:
                    if (password != ""):
                        status = map[username][1]
                        if (status == 1 or(map[username][0] != password)):
                            ans.append("Login Unsuccessful")
                        else:
                            map[username][1] = 1
                            ans.append("Logged In Successfully")
                    else:
                        ans.append("Login Unsuccessful")
            elif (action == "logout"):
                if (username not in map.keys()):
                    ans.append("Logged out Unsuccessful")
                else:
                    status = map[username][1]
                    if (status == 0):
                        ans.append("Logged out Unsuccessful")
                    else:
                      	map[username][1] = 0
                        ans.append("Logged out Successfully")
        return ans

obj = solution()
operations = [
    "register david david123",
    "register adam 1Adam1",
     "login david david123",
    "logout david",
    "login david david123",
    "login adam 1adam1",
    "logout david",
    "logout adam",
    "logout apple",
    "register banana",
    "logout zzz zzz",
    "register aa",
    "login zvvv",
    "register aa z",
    "login aa"
]
res = obj.userSystem(operations)
print(res)
```

####  Target_Words_Combined

- 给两个字符串s和t，求问使用s所有的字母最多能够重组出几个t。举个栗子：s=“mononom”，t=“mon”，则答案是2。

```python
class solution:
    def Target_Words_Combined(self, s:str, t:str) -> int:
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        for i in range(len(s)):
            cnt1[ord(s[i]) - ord('a')] += 1
        for j in range(len(t)):
            cnt2[ord(t[j]) - ord('a')] += 1
        ans = 0x3f3f3f3f
        for k in range(26):
            if (cnt2[k] != 0 and cnt1[k] != 0):
                ans = min(ans, cnt1[k] // cnt2[k])
        return ans
obj = solution()
s = "mononom"
t = "mon"
obj.Target_Words_Combined(s, t)
```

#### Gray_Graph

```python
def getMaximunGery(grid):
    prfSumRow = [0]*len(grid)
    prfSumCol = [0]*len(grid[0])
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c]=="1":  
               prfSumRow[r]+=1 
               prfSumCol[c]+=1
            else:                
               prfSumRow[r]-=1
               prfSumCol[c]-=1
            
    return max(prfSumRow)+max(prfSumCol)

class solution:
    def grey(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        grey_row = [0 for _ in range(row)]
        grey_col = [0 for _ in range(col)]
        for i in range(row):
            tmp = 0
            for char in matrix[i]:
                if (char == '1'):
                    tmp += 1
                else:
                    tmp -= 1
            grey_row[i] = tmp
        
        for j in range(col):   
            tmp = 0
            for i in range(row):
                if(matrix[i][j] == '1'):
                    tmp += 1
                else:
                    tmp -= 1
            grey_col[j] = tmp

        ans = -0x3f3f3f3f
        for i in range(row):
            for j in range(col):
                ans = max(grey_row[i]+grey_col[j], ans)
        return ans

obj = solution()
matrix = [
    "1101",
    "0101",
    "1010"
    ]
matrix2 = [
    "1001",
    "0111",
    "0001",
	]
obj.grey(matrix)
# reference 
# https://www.1point3acres.com/bbs/thread-844232-1-1.html
```

#### Change_Of_Temperature

- 计算Change of temperature eg: 假设三天的气温是[6, -2, 5] 第一天 max([6],[6+(-2)+5]) = max(6,9) = 9, 第二天 max([6+(-2)],[(-2)+5]]) = max(4,3) = 4, 第三天 max([6-2+5],[5]) = max(9,5) = 9, 最后return max(9,4,9)=9

```python
'''

6 -2 5

max(6, 6-2+5)
max(6-2, -2+5)
max(6-2+5, 5)

preSum
 [6,-2,5]
[0,6,4,9]

'''

class solution:
    def changeOfTemperature(self, arr):
        n = len(arr)
        preSum = [0] * (n + 1)
        for i in range(0, n):
            preSum[i + 1] = arr[i] + preSum[i]
        ans = -0x3f3f3f
        for i in range(1, n+1):
            ans = max(preSum[i] - preSum[0], preSum[n] - preSum[i - 1])
        return ans
      	
obj = solution()
arr = [6,-2,5]
obj.changeOfTemperature(arr)
```

#### Find_Minimum

- 给一组数组, 删掉k个连续元素, 问剩下最小的和是多少? eg: arr = [7, 3, 6, 1], k = 2, result = 7

```python
'''
    [7, 3, 6, 1]
  [0,7,10,16,17]
   l    r
'''
class solution:
    def maxDelete(self, k, arr):
        n = len(arr)
        preSum = [0] * (n + 1)
        ss = 0
        for i in range(0, n):
            preSum[i + 1] = preSum[i] + arr[i]
            ss += arr[i]
        
        left = 0 
        right = k 
        res = 0x3f3f3f3f
        while (right < n+1):
            total = preSum[right] - preSum[left]
            res = min(res, ss - total)
            left += 1
            right += 1
        return res
        
obj = solution()
obj.maxDelete(2, [7,3,6,1])
```

#### Maximum_Element_After_Decrementing_And_Rearranging

- 1开始的数组，后面每两个相邻数字直接差距不能>1，可以重新调整顺序和减少到>=1,问数组的最后一个数字可能的最大值

```python
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        '''
        [2,2,1,2,1]
         i j

        +- null/1 0/000 min/max odd/even repeated order/permutation
        '''
        
        arr.sort()
        if (arr[0] != 1):
            arr[0] = 1
        if (len(arr) < 2):
            return arr[0]
        n = len(arr)
        i = 0
        j = 1
        while (j < n):
            if (abs(arr[j] - arr[i]) >= 1):
                arr[j] = arr[i] + 1
            i += 1
            j += 1
        return max(arr)
```

#### Merge_Interval

- 最少merge几个区间, 返回的是int：Input: [[1,2],[2,3],[3,5],[4,5]]Output: 1，[4， 5] 被merge掉了， 所以是结果是1

```python
class Solution:
  	def mergeInterval(self, interval):
        '''
        排序以后 最早的结束的会最先出现 
          假设当前区间结束点为x 那么它留下的空白区域为[x:] 此时有另一个区间结束点为y并且x<y 那么它留下的空白区间为[y:]
          由于x<y 所以[y:] < [x:]
          留下的空间越大 那么删除就越少 因此可以贪心的得到结果
        '''
      	intervals.sort(key=lambda x: x[1])
        i = 0
        j = 0
        n = len(intervals)
        # 统计保留下来的区间
        cnt = 0
        while (i < n):
            j = i + 1
            while (j < n and intervals[j][0] < intervals[i][1]):
                j += 1
            cnt += 1    
            i = j
        return n - cnt
```

#### Min_Net_Stack

```python
class Solution:
    def minNetStack(self, arr):
        def get(l, r):
            return preSum[r] - preSum[l - 1] 
        
        n = len(arr)
        preSum = [0] * (n + 1)
        for i in range(0, n):
            preSum[i + 1] = arr[i] + preSum[i]
        
        res = 0
        tmp = float('inf')
        for i in range(0, n-1):
            leftVal = get(1,i+1) 
            rightVal = get(i+2,n) 
            
            leftVal //= (i + 1)
            rightVal //= (n - (i+1))
             
            if (abs(leftVal - rightVal) < tmp):
                tmp = abs(leftVal - rightVal)
                res = i+1
        return res
        

obj = Solution()
# arr = [1,3,2,3]
arr = [1,1,1,1,1,1]
obj.minNetStack(arr)
```

#### Number_of_Distinct_Subarrays_With_At_Most_K_Odd_Numbers

```python
class Solution:
  def NumOfDisSubWithAtMostKOddNum(arr, k):
    	cnt = 0
      seen = set()
      n = len(arr)
      for i in range(0, n):
       	countOdds = 0
        tmp = []
        for j in range(i, n):
          if(arr[j] % 2 == 1):
            countOdds += 1
          if (countOdds > k):
            break
          tmp.append(arr[j])
          tmpKey = tuple(tmp)
          if (tmpKey not in seen):
            seen.add(tmpKey)
            cnt += 1
       return cnt
    
obj = Solution()
arr = [3,2,3]
k = 1
obj.NumOfDisSubWithAtMostKOddNum(arr, k)
```

#### Common_Prefix

```python
class solution:
  def commonPrefix(self, inputs:str):
    l, r = 0, 0
    i = 1
    n = len(inputs)
    z = [0] * n
    for i in range(1, n):
        # i没有超过r
        if (z[i - l] < r - i + 1):
            z[i] = z[i - l]
        else:
        		# i超过了r
            z[i] = max(r - i + 1, 0)
            while (i + z[i] < n and inputs[z[i]] == inputs[i + z[i]]):
                z[i] += 1
            l = i
            r = i + z[i] - 1
    return sum(z) + n

obj = solution()
res = obj.commonPrefix("abcabcd")
```

#### Find_Max_In_K_Size_Subarray_With_No_Repeated

```python
class solution:
    def findMaxInKSizeSubarrayWithNoRepeated(self, arr, k: int):
        '''
        [1,2,7,7,4,3,6], k = 3
        i   j
        '''
        n = len(arr)
        preSum =[0] * (n+1)
        ll = 0
        rr = 0
        seen = set()
        tmp = []
        
        def get(l, r):
            return preSum[r] - preSum[l - 1]
        
        while (rr < n):
            preSum[rr+1] = preSum[rr] + arr[rr]
        
            while (ll < rr and arr[rr] in seen):
                seen.remove(arr[ll])
                ll += 1
            
            if (rr - ll + 1 == k):
                tmp.append([ll, rr])
                
            seen.add(arr[rr])
            rr += 1
        
        res = 0
        for x, y in tmp:
            res = max(res, get(x+1, y+1))
        return res

obj = solution()
arr = [1,2,7,7,4,3,6]
k = 3
obj.findMaxInKSizeSubarrayWithNoRepeated(arr, k)
```

#### Pascal_Triangle

```python
from typing import List;
class solution:
    def pascalTriangle(self, arr: List[int]) -> str:
        n = len(arr)
        for i in range(0, n-2):
            for j in range(0, n - i - 1):
                arr[j] = (arr[j] + arr[j + 1]) % 10
        
        return str(arr[0]) + str(arr[1])

obj = solution()
arr = [4,5,6,7,9]
res = obj.pascalTriangle(arr)
print(res)
```

#### Prime_Movie_Award

```python
class solution:
    def primeMovieAward(self, arr, k):
        arr.sort()
        i = 0
        j = 0
        n = len(arr)
        cnt = 0

        while (j < n):
            while (j < n and abs(arr[j] - arr[i]) <= k):
                j += 1
            cnt += 1
            i = j
        return cnt

obj = solution()
arr = [1, 5, 4, 6, 8, 9, 2, 1, 1, 2]
k = 3
res = obj.primeMovieAward(arr, k)
print(res)
```

#### Max_Consecutive_Number

```python
from typing import List

class solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        ll = 0
        rr = 0
        n = len(arr)
        res = 0
        while (rr < n):
            if (arr[rr] == 0):
                k -= 1
            while (k < 0):
                if (arr[ll] == 0):
                    k += 1
                ll += 1
            res = max(res, rr - ll + 1)
            rr += 1
        return res
    
obj = solution()
arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
k = 2
res = obj.longestOnes(arr, 2)
print(res)

```

#### Count_How_Many_Sub_Sequence_101_Or_010_In_The_String

- Given:A binary string that represents pages of a book (0011010). 1 represents a bookmarked page and 0 represents non-bookmarked flag.

  Find the number of ways to choose 3 pages (i, j, k) such that i < j < k and consecutive pages in the selection is not same.
  Valid selecitons: "010" and "101"
  Invalid selections: All other selections (110, 000, 111, etc.)

  

  Test Case 1:
  book: "00101"

  

  There are total 3 ways to choose pages which are "010", "010" and "101". So, the answer is 3.

```python
class solution:
    def countSubsequence101010(self, s:str) -> int:
        def dfs(i, j, s, tmp):
            if ((i < 0 and j < 0) or j < 0):
                return 1
            if (i < 0):
                return 0
            
            res = 0
            if (s[i] == tmp[j]):
                res += dfs(i-1, j-1, s, tmp)
                res += dfs(i-1, j, s, tmp)
            else:
                res += dfs(i-1, j, s, tmp)
                
            return res
        
        s1 = "101"
        s2 = "010"
        len1 = len(s1)
        len2 = len(s2)
        n = len(s)
        return dfs(n - 1, len1 - 1, s, s1) + dfs(n - 1, len2 - 1, s, s2)

obj = solution()
res = obj.countSubsequence101010("01001")
print(res)
```

#### Count_AZ

- 一个string，可以在任意位置添加一个字符，最多只能添加一个字符(A或Z)，问最多能组成多少个AZ，不能改变顺序

```python
import bisect
from typing import List


class solution:
    def countAZ(self, s:str) -> int:
        '''
        要么A加在最前面
        要么Z加在最后面

        A + frq(substring)
        frq(substring) + Z
        '''

        n = len(s)
        posA = []
        posZ = []
        for i in range(0, n):
            if (s[i] == 'A'):
                posA.append(i)
            elif (s[i] == 'Z'):
                posZ.append(i)
        print(posA)
        print(posZ)

        cnt = 0
        for idx in posA:
            tmp = bisect.bisect_left(posZ, idx)
            cnt += (len(posZ) - tmp)
        
        return cnt + len(posA) if len(posA) > len(posZ) else cnt + len(posZ)

obj = solution()
res = obj.countAZ("BAZAZ")
print(res)
```

#### [The_kth_Factor_Of_N](https://leetcode.cn/problems/the-kth-factor-of-n/)

```python
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        cnt = 0
        i = 1
        while (i <= n // i):
            if (n % i == 0):
                k -= 1
                if (k == 0):
                    return i
            i += 1
            
        # 注意，此时 i * i > n，所以要 i --
        i -= 1
        # 第二趟反向遍历，对 i 的初始值，还需要根据是否 i * i == n 做判断，避免重复
        if (i == n // i):
            i -= 1
            
        while (i > 0):
            if (n % i == 0):
                k -= 1
                if (k == 0):
                    return n // i
            i -= 1
        return -1
```

#### Router

- 给一个buildingCount array ，每个element代表一个building，上面的value代表这个building的人数 [1，4，2，3，2]就是第一个building有一个人，第二个有4个人，第三个有两个人... 

  第二个array 叫 routerLocation， 每个element代表router在哪个building，eg: [3，1] 就是说第一个router在building3，第二个在building1

  第三个array叫router Range 里面代表那个router能辐射的范围。[2，3] 第一个router能辐射前后两个building，如果它位于building3，那么就是1，2，3，4，5 都可以覆盖到。

  条件是，每个building被‍‌‍‍‍‌‌‌‌‌‌‍‍‌‍‍‌‌‌‍辐射的router的数量必须大于等于人数才能算能serve。问有几个building能被serve

```python
from typing import List
class solution:
    def router(self, buildingCount: List[int], routerLocation: List[int], routerRange: List[int]) -> int:
        
        n = len(buildingCount)
        tmp = [0] * (n+2)
        for i in range(0, len(routerLocation)):
            tmp[max(1, routerLocation[i] - routerRange[i])] += 1
            tmp[min(n+1, routerLocation[i] + routerRange[i] + 1)] -= 1
        # print(tmp)
        total = 0
        cnt = 0
        for i in range(1, len(buildingCount)):
            total += tmp[i]
            if (total >= buildingCount[i-1]):
                cnt += 1            
        return cnt

obj = solution()
a = [1,4,2,3,2]
b = [3,1]
c = [2,3]
res = obj.router(a, b, c) 
print(res)
```





### OA2





### VO





### Projects

- Around: GCP and React based Social NetworkAround: GCP and React based Social Network

  Feb 2022 - Present

  - ● Built a social network application based on React JS.
    ● Designed the features of posting and browsing according to classification.
    ● Handled users posts in Go and deployed to Google Cloud.
    ● Used token-based registration/login/logout flow with React Router v4 and server-side user authentication with JWT to improve the authentication.
    ● Used Elasticsearch for users to search and list posts.

- Twitch: A Personalized Twitch Resources Recommendation EngineTwitch: A Personalized Twitch Resources Recommendation Engine

  Dec 2021 - Jan 2022

  - [Show project](http://3.21.248.215/)

  - ● Built a full-stack web application for users to search streams, video and clips from Twitch resources and get recommendations.
    ● Designed the function of registration, login, logout and favorite.
    ● Constructed the project based on Spring MVC to dispatch servlets.
    ● Tested by Postman and handled the HTTP requests and responses by RESTful APIs.
    ● Fetched web resources by Twitch API and stored personal data in MySQL on Amazon RDS by Hibernate.
    ● Implemented resources recommendation by content-based algorithm.
    ● Built a web page with React and Ant Design to make it user friendly.
    ● Deployed the project on AWS EC2.

- Experimental Design of Network SwitchExperimental Design of Network Switch

  Jan 2021 - Feb 2021

  - ● Designed IP address and built communication with multiple routing devices according to requirement in GNS3 environment.
    ● Modified network configuration and tested RIP and OSPF on Linux environment.
    ● Used Wireshark to capture and analyze packets.