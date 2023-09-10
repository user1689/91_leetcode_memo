```
Pairs with Specific Difference
Given an array arr of distinct integers and a nonnegative integer k, write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, such that x - y = k. If no such pairs exist, return an empty array.

Note: the order of the pairs in the output array should maintain the order of the y element in the original array.

Examples:

input:  arr = [0, -1, -2, 2, 1], k = 1
output: [[1, 0], [0, -1], [-1, -2], [2, 1]]

input:  arr = [1, 7, 5, 3, 32, 17, 12], k = 17
output: []
Constraints:

[time limit] 5000ms

[input] array.integer arr

0 ≤ arr.length ≤ 100
[input]integer k

k ≥ 0
[output] array.array.integer
```

```Java
import java.io.*;
import java.util.*;

class Solution {

  static int[][] findPairsWithGivenDifference(int[] arr, int k) {
    // your code goes here
      
    // step1 store entry like {y: x} base on equation y = x - k
    Map<Integer, Integer> map = new HashMap<>(); // {element in array: index of it}
    
    // y = x - k
    // {x - k: x}
    // check key
    int n = arr.length;
    for (int i = 0; i < n; i++) {
      map.put(arr[i] - k, arr[i]); 
    }
    
    // iterate arr so that order can be same
    // step2 iterate input array and see if key exist in map, if existed, store it into answer array
    List<int[]> list = new ArrayList<>();
    for (int i = 0; i < n; i++) {
      if (map.containsKey(arr[i])) {
        list.add(new int[]{map.get(arr[i]), arr[i]}); // y exist, x definite exist 
      }
    }
    int[][] res = new int[list.size()][2];
    for (int i = 0; i < list.size(); i++) {
       res[i] = list.get(i);
    }
    return res;
  }

  public static void main(String[] args) {
    int[] testArr = new int[]{0, -1, -2, 2, 1};
    int k = 1;
    int[][] ans = findPairsWithGivenDifference(testArr, k);
    int n = ans.length;
    for (int i = 0; i < n; i++) {
      System.out.println(Arrays.toString(ans[i]));
    }
    
  }

}
```
