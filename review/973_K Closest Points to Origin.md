# [973\. K Closest Points to Origin](https://leetcode.cn/problems/k-closest-points-to-origin/)

## Description

Difficulty: **中等**  

Related Topics: [Geometry](https://leetcode.cn/tag/geometry/), [Array](https://leetcode.cn/tag/array/), [Math](https://leetcode.cn/tag/math/), [Divide and Conquer](https://leetcode.cn/tag/divide-and-conquer/), [Quickselect](https://leetcode.cn/tag/quickselect/), [Sorting](https://leetcode.cn/tag/sorting/), [Heap (Priority Queue)](https://leetcode.cn/tag/heap-priority-queue/)


Given an array of `points` where points[i] = [x<sub>i</sub>, y<sub>i</sub>] represents a point on the **X-Y** plane and an integer `k`, return the `k` closest points to the origin `(0, 0).

The distance between two points on the **X-Y** plane is the Euclidean distance (i.e., √(x<sub>1</sub> - x<sub>2</sub>)<sup>2</sup> + (y<sub>1</sub> - y<sub>2</sub>)<sup>2</sup>).

You may return the answer in **any order**. The answer is **guaranteed** to be **unique** (except for the order that it is in).

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/03/closestplane1.jpg)

``
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
```

**Example 2:**

```
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
```

**Constraints:**

*   1 <= k <= points.length <= 10<sup>4</sup>
*   -10<sup>4</sup> < x<sub>i</sub>, y<sub>i</sub> < 10<sup>4</sup>


## Solution

Language: Python

```python3
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        自定义比较项 01
        def compare(point):
            x, y = point
            return x**2 + y**2
        
        return sorted(points, key=compare)[:k]
        
        自定义比较项 02 
        return sorted(points, key=lambda x:x[0]*x[0]+x[1]*x[1])[:k]
        
        自定义比较方法
        cmp_to_key
        from functools import cmp_to_key 
        def cmp(x, y):
            tmp1 = x[0]*x[0] + x[1]*x[1]
            tmp2 = y[0]*y[0] + y[1]*y[1]
            return tmp1 - tmp2
        
        return sorted(points, key=cmp_to_key(cmp))[:k]
        
        自定义运算符 *这个的比较逻辑和其他几个略有不同 true or false
        class Node:
            def __init__(self, x):
                self.x = x
​
            def __lt__(self, other):
                tmp1 = self.x[0]*self.x[0]+self.x[1]*self.x[1]
                tmp2 = other.x[0]*other.x[0]+other.x[1]*other.x[1]
                return tmp1 < tmp2 if tmp1 != tmp2 else tmp1 > tmp2
                
            tmp = []
            for i in range(0, len(points)):
                tmp.append(Node(points[i]))
            tmp.sort()
            return [pair.x for pair in tmp[:k]]
​
        '''
        

```

```java
class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                int x1 = o1[0]*o1[0] + o1[1]*o1[1];
                int x2 = o2[0]*o2[0] + o2[1]*o2[1];
                return x1 - x2;
            }
        });
        for (int i = 0; i < points.length; i++) {
            pq.offer(points[i]);
        }
        int[][] res = new int[k][2];
        int j = 0;
        while (k > 0) {
            int[] tmp = pq.poll();
            res[j][0] = tmp[0];
            res[j][1] = tmp[1];
            j++;
            k--;
        }
        return res;
    }
}
```
