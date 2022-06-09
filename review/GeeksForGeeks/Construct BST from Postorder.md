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

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode bstFromPreorder(int[] preorder) {
        return constructTree(preorder, 0, preorder.length - 1);
    }
    
    public TreeNode constructTree(int[] preorder, int left, int right) {
        if (left == right) {
            return new TreeNode(preorder[left]);
        }
        if (left > right) {
            return null;
        }
        
        int rootVal = preorder[left];
        TreeNode root = new TreeNode(rootVal, null, null);
        int leftLastIndex = binarySearch(preorder, left+1, right, rootVal);
        
        root.left = constructTree(preorder, left+1, leftLastIndex);
        root.right = constructTree(preorder, leftLastIndex+1, right);
        
        return root;
    }
    
    public int binarySearch(int[] preorder, int left, int right, int x){
        /*
        
        [2] 找到最后一个小于2的 直接会return left;
        
        [4] 找到最后一个小于4的 直接会return left;
        
        [4,2] 找到最后一个小于4的 return 1;
        
        [2,4] 找到最后一个小于2的 x < preorder[left] { return left - 1; }
        
        [3,2,4] 找到最后一个小于3的 return 1;
        
        
        */
        if (left > right) {
            return left - 1;
        }
        if (x < preorder[left]) {
            return left - 1;
        }
        
        while (left < right) {
            int mid = (left + right + 1) >> 1;
            if (preorder[mid] < x) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
}
```

## 复杂度分析
* time nlogn
* space n

## 相关题目
1. 待补充
