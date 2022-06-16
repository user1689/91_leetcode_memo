# [590\. N-ary Tree Postorder Traversal](https://leetcode.cn/problems/n-ary-tree-postorder-traversal/)

## Description

Difficulty: **简单**  

Related Topics: [Stack](https://leetcode.cn/tag/stack/), [Tree](https://leetcode.cn/tag/tree/), [Depth-First Search](https://leetcode.cn/tag/depth-first-search/)


Given the `root` of an n-ary tree, return _the postorder traversal of its nodes' values_.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)

```
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png)

```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
```

**Constraints:**

*   The number of nodes in the tree is in the range [0, 10<sup>4</sup>].
*   0 <= Node.val <= 10<sup>4</sup>
*   The height of the n-ary tree is less than or equal to `1000`.

**Follow up:** Recursive solution is trivial, could you do it iteratively?


## Solution

Language: Java

```java
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;
​
    public Node() {}
​
    public Node(int _val) {
        val = _val;
    }
​
    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/
​
class Solution {
    public List<Integer> postorder(Node root) {
        List<Integer> res = new ArrayList<>();
        Deque<Node> stack = new ArrayDeque<>();
        Map<Node, Integer> map = new HashMap<>();
        
        while (!stack.isEmpty() || root != null) {
            while (root != null) {
                stack.offerLast(root);
                if (root.children != null && root.children.size() > 0) {
                    map.put(root, 0);
                    root = root.children.get(0);
                } else {
                    root = null;
                }
            }
            
            root = stack.peekLast(); // 这里不能像bst一样直接pop 因为还有其他的孩子节点
            int index = map.getOrDefault(root, -1) + 1; // 获取当前root的list遍历到哪里了
            List<Node> children = root.children; // 获取当前root的子节点list
            if (children != null && children.size() > index) {
                map.put(root, index); // 更新此root的孩子节点遍历到哪里了
                root = children.get(index);
            } else {
                // 当前root没有孩子节点了 把root本身加入res中
                res.add(root.val);
                map.remove(root);
                stack.pollLast();
                root = null;
            }
            
        }
        return res;
    
         
    }
}
```
