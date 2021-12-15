# Review of leetcode questions 1 to 400

合并
负数取余负数取模python3

负数取余负数取模java
floorMod



排列  排列结果
全排列 n!
普通排列 Pnk

全组合只有一种
组合  路径 
普通组合 Cnk （在路径中选择的数量满足k时提前返回）
重复组合 Hnm = (n+m-1)! / m!(n-1)!

子集
无重复子集 2**n > Cnk （遍历完所有路径）
重复子集 2**n 


python 
//取商 向负无穷取整取整 c = a // b
/取商 返回小数 c = a / b
%取模or取余  r = a - c * b = a - (a//b) * b 向负无穷取整取整 -7%3 =   -7 - 3*(-7//3) = 2

java
/取商 返回0取整 c = a / b
%取模or取余  r = a - c * b = a - (a/b) * b 向0取整 -7%3 =   -7 - 3*(-7/3) = -1


2147483647
-2147483648

快速乘/倍增乘法


概率类DP


DPS优化手段
长度大于10就要小心了 大于15,20一般都需要上DP或者需要DFS状态压缩等优化技巧了
记忆化搜索以后时间复杂度就和状态的数目有关
记忆化搜索的visited数组一般如果表示的数字在六个0位合适
注意是否会从头开始搜索如果从头开始搜索就需要用visited数组来避免重复剪枝就类似permutation unique  如果不会重头开始搜索就不需要用visited数组剪枝就类似 subset II
DFS求最少数量 成立的情况返回1 不成立返回-1 维护一个局部变量来获取本层合法的最小数量 
传入left right的DFS也可以考虑考虑
求间隔多少空格 和 求长度/个数计算方法不同 前者为right-left 后者为right-left+1
dfs传递参数控制的是深度 for控制的广度即当前层的展开

 
二进制转十进制  0010 = 0*2**0 + 1*2**1
八进制转十进制 
十六进制转十进制

十进制转二进制       49 // 2 = 24 … 1   24 // 2 = 12 … 0   12 // 2 =  6 … 0   6 // 2 = 3 … 0   3 // 2 = 1 … 1      0b110001
十进制转八进制
十进制转十六进制

二进值转八进制       1010101  = 001 | 010 | 101 = 1|2|5 = 0o125
二进值转十六进制   
八进制转十六进制(先转化成二进制再转化成十六进制)  0o125 = 001 | 010 | 101 =  0101| 0101 = 0x55

正数 原码=反码=补码
负数 原码 反码=原码取反  补码=反码+1
补码之间运算如果求得是正数 原码 = 反码 = 补码
补码之间运算如果求得是负数 需要求得原码再转化对应十进制 原码补码互为取反+1 


subarray很多题目都是固定一个边界寻找另外一个边界

Greedy：
1.Sweeping line / diff 
2.Sort 
sort by starting point => the minimum number of intervals to cover the whole 
sort by ending point => the maximum number of intervals that are non-overlapping
DP:


二分
1.二分左边界和二分右边界在单调递增数组上的答案是一样的但是在单调数组上比如[1,1,1,0,0]或[0,0,0,1,1,1]有些题目会要求出发方向比如求x的幂或者验证程序等都是从左往右发展出来的事物
2.如果二分左右界用不了可以考虑想想bisect的结果是否符合题目要求 想想他们之间的不同尝试代入看看 eg:[1,2,3,4,5,8] target = 5 bisect_right会返回5 而二分右边界会返回4

hashTable:
1.如果存坐标不行 可以试试看存数量 
2. 不一定要分开扫描 可以试试一次扫描 然后对位置不同的和位置相同的做不同的判断
3. 注意哈希表在扫的时候如果没有key存在会默认设置为0 不要忽略了 可以用于解题

unionFInd
1.并查集的初始化有很多方法 要分类掌握 比如如果双重for的内层for循环写成range(i,n)可能就需要做 setdefault等方法来避免遍历到这个key的时候不存在出现的key error
2.并查集的root定义中 可以定义root节点的父节点为root本身 或 root节点的父节点为None 不同的定义会影响到add和find方法
3.for i in range(n): for j in range(i)

graph
1.建图能力还需要提升

tricky:
1. for i in range(i, len(s) - len(p) + 1):  tmp = s[i : i+len(p)]
2. spiral+rotate image
3. row, col:  matrix[i][j]  —> arr[i*col+j]

实现一个deque

all True 
any False
