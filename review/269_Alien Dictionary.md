## 题目
https://www.lintcode.com/problem/892/description

## 思路
topological sort

```java
public class Solution {
    /**
     * @param words: a list of words
     * @return: a string which is correct order
     */
    public String alienOrder(String[] words) {
        // Write your code here
        Map<Character, Set<Character>> edges = new HashMap<>();
        Map<Character, Integer> inDegrees = new HashMap<>();
        for (String s : words) {
            for (char c : s.toCharArray()) {
                inDegrees.putIfAbsent(c, 0);
            }
        }
        
        // build graph
        for (int i = 0; i < words.length - 1; i++) {
            String s1 = words[i];
            String s2 = words[i+1];
            int len = Math.min(s1.length(), s2.length());
            // case like: ["abc","ab"] 
            if (s1.substring(0, len).equals(s2)) return "";
            for (int j = 0; j < len; j++) {
                char c1 = s1.charAt(j);
                char c2 = s2.charAt(j);
                if (c1 == c2) continue;
                Set<Character> tmpSet = edges.getOrDefault(c1, new HashSet());
                if (!tmpSet.contains(c2)) {
                    // error 1: if the value of map is a set or list, if you want to add value into set or list, follow the next steps.
                    // list or set = getOrDefault -> list or set invoke add method -> map.put(key, list or set)
                    tmpSet.add(c2);
                    edges.put(c1, tmpSet);
                    inDegrees.put(c2, inDegrees.get(c2) + 1);
                }
                break;
            }
        }

        // build heap
        PriorityQueue<Character> heap = new PriorityQueue<>(new Comparator<Character>(){
            @Override
            public int compare(Character c1, Character c2) {
                return c1 - c2;
            }
        });

        // offer element which indegree is 0
        for (Map.Entry<Character, Integer> entry : inDegrees.entrySet()) {
            if (entry.getValue() == 0) heap.offer(entry.getKey());
        }

        // topological sort
        StringBuilder sb = new StringBuilder();
        while (!heap.isEmpty()) {
            Character c = heap.poll();
            sb.append(c);
            Set<Character> edge = edges.getOrDefault(c, new HashSet());
            for (Character cc : edge) {
                inDegrees.put(cc, inDegrees.get(cc) - 1);
                if (inDegrees.get(cc) == 0) {
                    heap.offer(cc);
                }
            }
        }
 
        return sb.length() == inDegrees.size() ? sb.toString() : "";
    }
}
```
