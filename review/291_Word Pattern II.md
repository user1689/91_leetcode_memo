## 题目
https://leetcode.cn/problems/word-pattern-ii  
https://kennyzhuang.gitbooks.io/leetcode-lock/content/291_word_pattern_ii.html

## 思路
dfs

## java
```java
import java.util.HashMap;
import java.util.Map;

public class wordPatternMatch {
  
  public static void main(String[] args) {
    boolean res = findWordPatternMatch("aaaa", "asdasdasdasd");
    System.out.println(res);
  }

  public static boolean findWordPatternMatch(String pattern, String str) {
    Map<Character, String> pts = new HashMap<>();
    Map<String, Character> stp = new HashMap<>();
    return helper(0, 0, pattern, str, pts, stp);
  }

  public static boolean helper(int startIdx, int ptr, String pattern, String str, Map<Character, String> pts, Map<String, Character> stp) {

    if (ptr == pattern.length() && startIdx == str.length()) {
      return true;
    }

    if (ptr >= pattern.length() || startIdx >= str.length()) {
      return false;
    }
    

    for (int i = startIdx; i < str.length(); i++) {
      char c = pattern.charAt(ptr);
      String sub = str.substring(startIdx, i+1);
      if ( !stp.containsKey(sub) 
        || !pts.containsKey(c) 
        || (stp.containsKey(sub) && stp.get(sub) == c) 
        || (pts.containsKey(c) && pts.get(c).equals(sub))
      ) {
        pts.put(c, sub);
        stp.put(sub, c);
        if (helper(i+1, ptr+1, pattern, str, pts, stp)) {
          return true;
        }
        pts.remove(c);
        stp.remove(sub);
      }
    }
    return false;
  }

}

```

## 复杂度分析
* time 2^n
* space n

## 相关题目
1. 待补充
