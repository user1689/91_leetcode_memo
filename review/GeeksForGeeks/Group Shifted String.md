## 题目
https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/group-shifted-string-official/ojquestion

## Java
```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

class GroupShiftedString {

  public static ArrayList<ArrayList<String>> groupShiftedStrings(String[] strs) {
    // write your code here
    Map<String, ArrayList<String>> map = new HashMap<String, ArrayList<String>>();
        ArrayList<ArrayList<String>> res = new ArrayList<>();
        for (String word : strs) {
            String key = hashCode(word);
            ArrayList<String> tmp = map.getOrDefault(key, new ArrayList<>());
            tmp.add(word);
            map.put(key, tmp);
        }
        for (Map.Entry<String, ArrayList<String>> entry : map.entrySet()) {
            res.add(entry.getValue());
        }
   
    return res;
  }
  
  static String hashCode(String s) {
      StringBuilder sb = new StringBuilder();
      int target = s.charAt(0) - 'a';
      sb.append(0);
      sb.append(",");
      for (int i = 1; i < s.length(); i++) {
          int t = s.charAt(i) - 'a';
          t = ((t - target) % 26 + 26) % 26;
          sb.append(t);
          sb.append(",");
      } 
      return sb.toString();
  }
  
  public static void main(String[] args) {

    String[] arr = new String[]{"acd", "dfg", "wyz", "yab", "mop" ,"bdfh" ,"a" ,"x" ,"moqs"};
    ArrayList<ArrayList<String>> shiftedGroup = groupShiftedStrings(arr);
    for (ArrayList<String> lst : shiftedGroup) {
      System.out.println(lst.toString());
    }
    
  }

}
``` 
