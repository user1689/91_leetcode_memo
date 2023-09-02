```
Word Count Engine
Implement a document scanning function wordCountEngine, which receives a string document and returns a list of all unique words in it and their number of occurrences, sorted by the number of occurrences in a descending order. If two or more words have the same count, they should be sorted according to their order in the original sentence. Assume that all letters are in english alphabet. You function should be case-insensitive, so for instance, the words “Perfect” and “perfect” should be considered the same word.

The engine should strip out punctuation (even in the middle of a word) and use whitespaces to separate words.

Analyze the time and space complexities of your solution. Try to optimize for time while keeping a polynomial space complexity.

Examples:

input:  document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"

output: [ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"], 
          ["get", "1"], ["by", "1"], ["just", "1"] ]
Important: please convert the occurrence integers in the output list to strings (e.g. "3" instead of 3). We ask this because in compiled languages such as C#, Java, C++, C etc., it’s not straightforward to create mixed-type arrays (as it is, for instance, in scripted languages like JavaScript, Python, Ruby etc.). The expected output will simply be an array of string arrays.

Constraints:

[time limit] 5000ms
[input] string document
[output] array.array.string
```

```java
import java.io.*;
import java.util.*;

class wordCount {

  static String[][] wordCountEngine(String document) {
    // your code goes here
    Map<String, Integer> idxMap = new HashMap<>();
    Map<String, Integer> countMap = new HashMap<>();
    int j = 0;
    int n = document.length();
    // step1 count 
    StringBuilder sb = new StringBuilder();
    while (j < n) {
      char c = document.charAt(j);
      //                        j  
      // Practice makes perfect.
      if (Character.isLetter(c)) {
        // practice, makes
        sb.append(Character.toLowerCase(c));
      } else if (c == ' ') {
        String tmpStr = sb.toString();
        countMap.put(tmpStr, countMap.getOrDefault(tmpStr, 0) + 1); // int -> Integer
        if (!idxMap.containsKey(tmpStr)) {
          idxMap.put(tmpStr, j);
        }
        sb = new StringBuilder();
      }
      j++;
    }
    String tmpStr = sb.toString();
    countMap.put(tmpStr, countMap.getOrDefault(tmpStr, 0) + 1);
    if (!idxMap.containsKey(tmpStr)) idxMap.put(tmpStr, j);
    
    // step2 build 
    String[][] res = new String[countMap.size()][2];
    int idx = 0;
    for (Map.Entry<String, Integer> element : countMap.entrySet()) {
      res[idx][0] = element.getKey();
      res[idx][1] = String.valueOf(element.getValue());
      idx++;
    }
    // step3 sort
    Arrays.sort(res, new Comparator<String[]>() {
      @Override
      public int compare(String[] e1, String[] e2) {
        String key1 = e1[0];
        String key2 = e2[0];
        int freq1 = countMap.getOrDefault(key1, 0);
        int freq2 = countMap.getOrDefault(key2, 0);
        if (freq1 == freq2) {
          return idxMap.getOrDefault(key1, 0) - idxMap.getOrDefault(key2, 0);
        } else {
          return freq2 - freq1;
        }
      }
    });
    return res;
  }
   
  /*
     0     1    2    3     
  "apple only only apple"
  */

  public static void main(String[] args) {
    String s = "Practice makes perfect. you'll only get Perfect by practice. just practice!";
    String[][] res = wordCountEngine(s);
    for (String[] x : res) {
      System.out.println(Arrays.toString(x));
    }
  }

}


// map2 = {practice: 0, makes: 1, perfec: 2, you'll: 3 ...}
// map1 = {practice: 1, makes: 1, perfect : 1, you'll: 1 ...}
// "Practice makes perfect. you'll only get Perfect by practice. just practice!"
```

```java
import java.io.*;
import java.util.*;

class Solution {

  static String[][] wordCountEngine(String document) {
    // your code goes here
    // step1 map1 for counting, map2 for original order
    Map<String, Integer> counter = new HashMap<>(); // dict
    Map<String, Integer> order = new HashMap<>();

    // step2 traverse
    String[] strArr = document.split(" ");
    int n = strArr.length;
    for (int i = 0; i < n; i++) {
      String tmpStr = strArr[i];
      String tmpAfter = filter(tmpStr);
      if ("".equals(tmpAfter)) continue;
      counter.put(tmpAfter, counter.getOrDefault(tmpAfter, 0) + 1);
      order.putIfAbsent(tmpAfter, i);
    }
    System.out.println(counter);
    
    // step3 build ans array, and extract entry from map
    String[][] ans = new String[counter.size()][2];
    int idx = 0;
    for (Map.Entry<String, Integer> entry : counter.entrySet()) {
      ans[idx][0] = String.valueOf(entry.getKey());
      ans[idx][1] = String.valueOf(entry.getValue());
      idx++;
    }
    
    // step4 sorted it base on topic
    Arrays.sort(ans, (e1, e2) -> {
      // freq are same
      if (e1[1].equals(e2[1])) {
        return Integer.valueOf(order.get(e1[0])) - Integer.valueOf(order.get(e2[0]));
      }
      return Integer.valueOf(counter.get(e2[0])) - Integer.valueOf(counter.get(e1[0]));
    });
    //for (int i = 0; i < ans.length; i++) {
    //  System.out.print(Arrays.toString(ans[i]));
    //}
    return ans;
  }
  
  static String filter(String s) {
    //System.out.println(s);
    StringBuilder sb = new StringBuilder();
    for (char c : s.toCharArray()) {
      if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) {
        sb.append(Character.toLowerCase(c));
      }
    }
    return sb.toString();
  }

  public static void main(String[] args) {
      //String testStr = "you;ll's";
      //String ansStr = filter(testStr);
      //System.out.println("expected: youlls, actual:" + ansStr);
    String document = "Every book is a quotation; and every house is a quotation out of all forests, and mines, and stone quarries; and every man is a quotation from all his ancestors. ";
    String[][] ans = wordCountEngine(document);
    for (int i = 0; i < ans.length; i++) {
      System.out.print(Arrays.toString(ans[i]));
    }
  }

}
/*
  
  O(nlogn)
 
  pattern1 sort by freqency
  pattern2 sort by original order if two or more words has same freqency
  
  case insensitive
  skip punctuation
  
  

*/
```
