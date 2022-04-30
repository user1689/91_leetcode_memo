## 题目
https://practice.geeksforgeeks.org/problems/union-find/1/

## 思路
并查集

## python3
```python3
#User function Template for python3

class Solution:
    
    def find_normal(self, x, p):
        if (x != p[x]):
            # return self.find_normal(p[x], p)
            p[x] = self.find_normal(p[x], p)
        return p[x]
    
    #Function to merge two nodes a and b.
    def union_(self,a,b,par,rank1):
        # code here
        if (self.find_normal(a, par) != self.find_normal(b, par)):
            # 链接两个节点的父节点
            par[self.find_normal(a, par)] = self.find_normal(b, par)
        

    #Function to check whether 2 nodes are connected or not.
    def isConnected(self,x,y,par,rank1):
        # code here
        if (self.find_normal(x, par) != self.find_normal(y, par)):
            return 0
        else:
            return 1
```
