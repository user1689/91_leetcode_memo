## Amazon OA



### OA1

#### Nine_Box

- 给一串字符，"abcdefgabc"，然后用手机九宫格打出。手机九宫格可以是任何字母组合，唯一要求是每个键至少有两个字母，最多三个字母。换句话说，这里的键位不一定是我们常见的2=abc，3=def等等，可以是1=agq，2=bhj...任何顺序都可以。要求找出能打出输入字符串的最少按键次数。

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
            
            if ((j - i) == k):
                ans = max(ans, prefix_sum[j] - prefix_sum[i])
                if (i < n):
                    seen.remove(arr[i])
                    i += 1
                    
            
            seen.add(arr[j])
            j += 1
        
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
k = 6
obj.max_average_stock_price(arr, k)
```







### OA2





### VO