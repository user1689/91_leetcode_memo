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
