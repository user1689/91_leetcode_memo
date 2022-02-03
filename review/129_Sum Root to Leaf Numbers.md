## 题目
https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/

## 思路
DFS

## python3
```python3
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
    public int sumNumbers(TreeNode root) {
        if(root == null) {
            return 0;
        }
        int sum = 0;
        Queue<TreeNode> queueNode = new LinkedList<>();
        Queue<Integer> queueNum = new LinkedList<>();
        queueNode.offer(root);
        queueNum.offer(root.val);
        while (!queueNode.isEmpty()) {
            TreeNode node = queueNode.poll();
            int num = queueNum.poll();
            if ((node.left == null) && (node.right == null)) {
                sum += num;
            } else {
                if (node.left != null) {
                    queueNode.offer(node.left);
                    queueNum.offer(num * 10 + node.left.val);
                }
                if (node.right != null) {
                    queueNode.offer(node.right);
                    queueNum.offer(num * 10 + node.right.val);
                }
            }
        }
        return sum;
    }
}
```

## 复杂度分析
* time n
* space logn

## 相关题目
1. 待补充
