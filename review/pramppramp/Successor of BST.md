# question
https://www.lintcode.com/problem/448/

# java
```java
// method 1 O(h)
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */


public class Solution {
    /*
     * @param root: The root of the BST.
     * @param p: You need find the successor node of p.
     * @return: Successor of p.
     */ 
    
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        // write your code here
        TreeNode cand = null;
        
        while (root != null) {
            if (p.val >= root.val) {
                root = root.right;
            } else {
                cand = root;
                root = root.left;
            }
        }
        
        return cand;
    }
}



// method 2 O(N)
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */


public class Solution {
    /*
     * @param root: The root of the BST.
     * @param p: You need find the successor node of p.
     * @return: Successor of p.
     */ 
    
    TreeNode prev;
    TreeNode res;
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        // write your code here
        dfs(root, p);
        return res;
    }
    public void dfs(TreeNode root, TreeNode p) {
        if (root == null) return ; 

        dfs(root.left, p);

        if (prev != null && prev == p) {
            res = root;
        } 
        prev = root;

        dfs(root.right, p);
    }
}
```
