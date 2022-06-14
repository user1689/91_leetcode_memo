## 题目
https://leetcode.cn/problems/longest-absolute-file-path/

## 思路
map, stack

## Java
```java
class Solution {
    public int lengthLongestPath(String input) {
        /*
        
        步骤一 按照\n进行划分
        步骤二 统计\t的数量表示在第几个level
        步骤三 通过一个哈希表来进行层级划分
        
        */
        Map<Integer, String> map = new HashMap<>();
        int n = input.length();
        String ans = null;
        for (int i = 0; i < n; ) {
            int level = 0;
            while (i < n && input.charAt(i) == '\t' && ++level >= 0) {
                i++;
            }
            boolean isDir = true;
            int j = i;
            while (j < n && input.charAt(j) != '\n') {
                if (input.charAt(j) == '.') {
                    isDir = false;
                }
                j++;
            }
            String cur = input.substring(i, j);
            String prev = map.getOrDefault(level - 1, null);
            String path = prev == null ? cur : prev + "/" + cur;
            if (isDir) map.put(level, path);
            else if (ans == null || path.length() > ans.length()) ans = path;
            i = j + 1;
            
        }
        
        return ans == null ? 0 : ans.length();
    }
}
```

## 复杂度分析
* time O(N)
* space O(N)

## 相关题目
1. 待补充
