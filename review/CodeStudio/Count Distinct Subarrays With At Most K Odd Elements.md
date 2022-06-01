## 题目
https://www.codingninjas.com/codestudio/problems/count-distinct-subarrays-with-at-most-k-odd-elements_1069335?leftPanelTab=0

## Java
```java
import java.util.HashSet;
public class Solution {
    public static int distinctSubKOdds(int[] arr, int n, int k) {
        // Write your code here
        Integer cnt = 0;
        HashSet<String> set = new HashSet<>();
        for (int i = 0; i < n; i++) {
            Integer countOdds = 0;
            StringBuilder sb = new StringBuilder();
            for (int j = i; j < n; j++) {
                if (arr[j] % 2 == 1) {
                    countOdds++;
                }
               
                if (countOdds > k) {
                    break;
                }
               
                sb.append(arr[j] + " ");
                
                if (!set.contains(sb.toString())) {
                    set.add(sb.toString());
                    cnt ++;
                }
            }

        }
        return cnt;
    }
}
```
