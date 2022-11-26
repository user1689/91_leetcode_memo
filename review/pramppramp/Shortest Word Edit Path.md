```
Shortest Word Edit Path
Given two words source and target, and a list of words words, find the length of the shortest series of edits that transforms source to target.

Each edit must change exactly one letter at a time, and each intermediate word (and the final target word) must exist in words.

If the task is impossible, return -1.

Examples:

source = "bit", target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]

output: 5
explanation: bit -> but -> put -> pot -> pog -> dog has 5 transitions.
source = "no", target = "go"
words = ["to"]

output: -1
Constraints:

[time limit] 5000ms
[input] string source
1 ≤ source.length ≤ 20
[input] string target
1 ≤ target.length ≤ 20
[input] array.string words
1 ≤ words.length ≤ 20
[output] array.integer
```

```java
import java.io.*;
import java.util.*;

class Solution {
	static Set<String> set;
	static Set<String> visited;
	static int shortestWordEditPath(String source, String target, String[] words) {
	    set = new HashSet<>();
	    for (String x : words) set.add(x);
	    if (!set.contains(target)) return -1;
	    visited = new HashSet<>();
	    visited.add(source); 
	    int res = dfs(source, target);
	    return res == set.size() + 1 ? -1 : res;
	}
  
	static int dfs(String cw, String ew) {
		if (ew.equals(cw)) {
			return 0;
		}

		int res = set.size() + 1;
		for (int i = 0; i < cw.length(); i++) 
		{
			char[] charArr = cw.toCharArray();
			for (int j = 0; j < 26; j++) 
			{
			    charArr[i] = (char) (j + 'a');
			    String tmpStr = new String(charArr);
			    if (set.contains(tmpStr) && !visited.contains(tmpStr) && !tmpStr.equals(cw)) 
			    {
				visited.add(tmpStr);
				res = Math.min(res, dfs(tmpStr, ew) + 1); 
				visited.remove(tmpStr);
			    }
			}
		}

    		return res;
  	}

	public static void main(String[] args) {
	    String source = "bit";
	    String target = "dog";
	    String[] words = new String[]{"but", "put", "big", "pot", "pog", "dog", "lot"};
	    int res = shortestWordEditPath(source, target, words);
	    System.out.println(res);
	}
}

```

```javascript
/*
 * 
 * 
 * 
Question
Shortest Word Edit Path
Given two words source and target, and a list of words words, find the length of the shortest series of edits that transforms source to target.

Each edit must change exactly one letter at a time, and each intermediate word (and the final target word) must exist in words.

If the task is impossible, return -1.

source = "bit", target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
 * */

function shortestWordEditPath(source, target, words) {

  //using WordsSet to keep track of visited set
  let minCount = Infinity;
  let WordsSet = new Set(words);

  if(!WordsSet.has(target)) return -1;
  if(target.length != source.length) return -1;
 
  function getMinCount(newWord, wordsSet) {
      //if(count > newWord.length) return;
    if(newWord === target) {
      return 0;
    }

    let wordArray = newWord.split("");
    let curMinCount = Infinity;
    for(let j= 0; j<newWord.length; j++) {
      for(let i =97; i<=122; i++) {
        if(i != wordArray[j].charCodeAt()) {
          wordArray[j] = String.fromCharCode(i);
          let newWord = wordArray.join("");
          if(WordsSet.has(newWord)) {
            WordsSet.delete(newWord);
            curMinCount = Math.min(getMinCount(newWord, WordsSet)+1, curMinCount);
            WordsSet.add(newWord);
          }
        }
        wordArray[j] = newWord[j];
      }
    }

    return curMinCount;
  }
  
  return getMinCount(source, WordsSet);
}
```
