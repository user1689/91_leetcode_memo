```
Sales Path
The car manufacturer Honda holds their distribution system in the form of a tree (not necessarily binary). The root is the company itself, and every node in the tree represents a car distributor that receives cars from the parent node and ships them to its children nodes. The leaf nodes are car dealerships that sell cars direct to consumers. In addition, every node holds an integer that is the cost of shipping a car to it.

Take for example the tree below:

alt

A path from Honda’s factory to a car dealership, which is a path from the root to a leaf in the tree, is called a Sales Path. The cost of a Sales Path is the sum of the costs for every node in the path. For example, in the tree above one Sales Path is 0→3→0→10, and its cost is 13 (0+3+0+10).

Honda wishes to find the minimal Sales Path cost in its distribution tree. Given a node rootNode, write a function getCheapestCost that calculates the minimal Sales Path cost in the tree.

Implement your function in the most efficient manner and analyze its time and space complexities.

For example:

Given the rootNode of the tree in diagram above

Your function would return:

7 since it’s the minimal Sales Path cost (there are actually two Sales Paths in the tree whose cost is 7: 0→6→1 and 0→3→2→1→1)

Constraints:

[time limit] 5000ms

[input] Node rootNode

0 ≤ rootNode.cost ≤ 100000
[output] integer
```

```java
import java.io.*;
import java.util.*;

class Solution {
 
  static class Node {
      
    int cost;
    Node[] children;
    Node parent;

    Node(int cost) {
      this.cost = cost;
      children = null;
      parent = null;
    }
  }

  // return mini cost start from current node to leaf node
  static class SalesPath {
    int getCheapestCost(Node rootNode) {
      // your code goes here
      if (rootNode.children == null) return rootNode.cost;
      
      int miniCost = Integer.MAX_VALUE;
      for (Node child : rootNode.children) {
        miniCost = Math.min(getCheapestCost(child), miniCost);
      }
      return miniCost + rootNode.cost;
    }
  }
    
  /*********************************************
   * Driver program to test above method     *
   *********************************************/

  public static void main(String[] args) {
    Node root = new Node(0);
    Node node1 = new Node(5);
    Node node2 = new Node(3);
    Node node3 = new Node(6);
    Node node4 = new Node(2);
    Node node5 = new Node(0);
    Node node6 = new Node(1);
    root.children = new Node[]{node1, node2, node3};
    node2.children = new Node[]{node4, node5, node6};
    Solution.SalesPath tmp = new Solution.SalesPath();
    int x = tmp.getCheapestCost(root);
    System.out.println(x);
  }
}
```
