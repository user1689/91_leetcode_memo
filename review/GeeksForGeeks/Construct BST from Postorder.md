## 题目
https://practice.geeksforgeeks.org/problems/construct-bst-from-post-order/1#

## 思路

## python3
```python3
#User function Template for python3

class Solution:
    def constructTree(self,post,n):
        # code here
        # find the first element smaller than post[idx]
        def binarySearch(first, last, cut):
            #  If the segment is empty, or the first value is larger than cut,
            #  by the assumptions, there is no value smaller than cut in the segment,
            #  return the position one before the start of the segment
            if ((last < first) or (post[first] > cut)):
                return first - 1
                
            low, high = first, last
            
            while (low < high):
                mid = (low + high + 1) >> 1
                if (post[mid] <= cut):
                    low = mid
                else:
                    high = mid - 1
            return low
        
        def construct(leftIdx, rightIdx):
            if (leftIdx > rightIdx):
                return None
                
            if (leftIdx == rightIdx):
                return Node(post[leftIdx])
        
            rootVal = post[rightIdx]
            root = Node(rootVal)
            
            leftLastIdx = binarySearch(leftIdx, rightIdx-1, rootVal)
            
            root.left = construct(leftIdx, leftLastIdx)
            root.right = construct(leftLastIdx + 1, rightIdx - 1)
            
            return root
        
        return construct(0, len(post) - 1)
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
   def __init__(self,val):
       self.val=val
       self.left=None
       self.right=None
class BST:
   size=0
   def inorder(self,tmp,size=0):
       if tmp:
           self.inorder(tmp.left,self.size)
           print(tmp.val,end=" ")
           self.inorder(tmp.right,self.size)
     
if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        obj=Solution()
        b=BST()
        pt=obj.constructTree(arr,n)
        b.inorder(pt)
        print()

# } Driver Code Ends
```

## 复杂度分析
* time nlogn
* space n

## 相关题目
1. 待补充
