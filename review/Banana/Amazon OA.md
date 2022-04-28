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



### OA2





### VO