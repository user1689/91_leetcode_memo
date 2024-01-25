## Topic
```
Diff Between Two Strings
Given two strings of uppercase letters source and target, list (in string form) a sequence of edits to convert from source to target that uses the least edits possible.

For example, with strings source = "ABCDEFG", and target = "ABDFFGH" we might return: ["A", "B", "-C", "D", "-E", "F", "+F", "G", "+H"

More formally, for each character C in source, we will either write the token C, which does not count as an edit; or write the token -C, which counts as an edit.

Additionally, between any token that we write, we may write +D where D is any letter, which counts as an edit.

At the end, when reading the tokens from left to right, and not including tokens prefixed with a minus-sign, the letters should spell out target (when ignoring plus-signs.)

In the example, the answer of A B -C D -E F +F G +H has total number of edits 4 (the minimum possible), and ignoring subtraction-tokens, spells out A, B, D, F, +F, G, +H which represents the string target.

If there are multiple answers, use the answer that favors removing from the source first.

Constraints:

[time limit] 5000ms
[input] string source
2 ≤ source.length ≤ 12
[input] string target
2 ≤ target.length ≤ 12
[output] array.string
```

## Solution
DP, DFS + Memorization

## Java
```Java
import java.io.*;
import java.util.*;

class Solution {
  static List<List<String>> res;
	static String[] diffBetweenTwoStrings(String source, String target) {
		// your code goes here
    // step1
    res = new ArrayList<>();
    List<String> path = new ArrayList<>();
    helper(0, 0, source, target, path);
    
    // step2
    String[] ans = null;
    for (int i = 0; i < res.size(); i++) {
      String[] tt = res.get(i).stream().toArray(String[]::new);
      if (ans == null || ans.length > tt.length) {
        ans = tt;
      }
    }
    
    return ans;
	}
  
  static void helper(int i, int j, String s, String t, List<String> path) {
    List<String> tmp = new ArrayList<>();
    if (i == s.length()) {
      for (String e : path) {
        tmp.add(e);
      }
      if (j != t.length()) {
        for (int k = j; k < t.length(); k++) {
          tmp.add("+" + t.charAt(k));
        }
      }
      res.add(tmp);
      return ;
    }
    if (j == t.length()) {
      for (String e : path) {
        tmp.add(e);
      }
      if (i != s.length()) {
        for (int k = i; k < s.length(); k++) {
          tmp.add("-" + s.charAt(k));
        }
      }
      res.add(tmp);
      return ;
    }
    
    // -a -b -c 
    //    i
    // abc
    //    j
    // abcdef
    
    if (s.charAt(i) != t.charAt(j)) {
      path.add("-" + s.charAt(i));
      helper(i + 1, j, s, t, path);
      path.remove(path.size() - 1);
      
      path.add("+" + t.charAt(j));
      helper(i, j + 1, s, t, path);
      path.remove(path.size() - 1);
    } else {
      path.add("" + s.charAt(i));
      helper(i + 1, j + 1, s, t, path);      
      path.remove(path.size() - 1);
    }
    
  }

	public static void main(String[] args) {
    String a = "CBBC";
    String b = "CABAABBC";
	  String[] ans = diffBetweenTwoStrings(a, b);
    System.out.println("ans = " + Arrays.toString(ans));
	}
}

```
