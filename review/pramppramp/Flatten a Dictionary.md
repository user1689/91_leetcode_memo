```
Flatten a Dictionary
A dictionary is a type of data structure that is supported natively in all major interpreted languages such as JavaScript, Python, Ruby and PHP, where it’s known as an Object, Dictionary, Hash and Array, respectively. In simple terms, a dictionary is a collection of unique keys and their values. The values can typically be of any primitive type (i.e an integer, boolean, double, string etc) or other dictionaries (dictionaries can be nested). However, for this exercise assume that values are either an integer, a string or another dictionary.

Given a dictionary dict, write a function flattenDictionary that returns a flattened version of it .

If you’re using a compiled language such Java, C++, C#, Swift and Go, you may want to use a Map/Dictionary/Hash Table that maps strings (keys) to a generic type (e.g. Object in Java, AnyObject in Swift etc.) to allow nested dictionaries.

If a certain key is empty, it should be excluded from the output (see e in the example below).

Example:

input:  dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }

output: {
            "Key1" : "1",
            "Key2.a" : "2",
            "Key2.b" : "3",
            "Key2.c.d" : "3",
            "Key2.c.e" : "1"
        }
Important: when you concatenate keys, make sure to add the dot character between them. For instance concatenating Key2, c and d the result key would be Key2.c.d.

Constraints:

[time limit] 5000ms
[input] Dictionary dict
[output] Dictionary
```

```java
import java.io.*;
import java.util.*;

class flattenMap {
	
  static HashMap<String, String> newMap;
  static HashMap<String, String> flattenDictionary(HashMap<String, Object> dict) {
    // your code goes here
    newMap = new HashMap<>();
    helper(dict, new ArrayList<>());
    return newMap;
  }
  static void helper(HashMap<String, Object> map, List<String> path) {
    
    for (Map.Entry<String, Object> entry : map.entrySet()) {
      if (entry.getValue() instanceof Map) {
        if (!"".equals(entry.getKey())) {
          path.add(entry.getKey());
        }
        helper((HashMap<String,Object>)entry.getValue(), path);
        if (path.size() > 0) path.remove(path.size() - 1);
      } else {
        
        String newKey = entry.getKey();
        StringBuilder sb = new StringBuilder();
        if (!"".equals(newKey)) {
          sb.insert(0, newKey);
          if (path.size() > 0) sb.insert(0,".");
        }
        for (int i = path.size() - 1; i >= 0; i--) {
          if (i == 0) {
            sb.insert(0, path.get(i));
          } else {
            sb.insert(0, path.get(i));
            sb.insert(0, ".");
          }
        }
        System.out.println(newKey);
        newMap.put(sb.toString(), (String) entry.getValue());
        
      }
    }
  }

  public static void main(String[] args) {
    HashMap<String, Object> map = new HashMap<>();
    HashMap<String, Object> map2 = new HashMap<>();
    map.put("Key1", "1");
    map2.put("a","2");
    map2.put("b","3");
    map.put("Key2", map2);
    HashMap<String, String> resMap = flattenDictionary(map);
    for (Map.Entry<String, String> entry : resMap.entrySet()) {
      System.out.println(entry.getKey()+" " + entry.getValue());
    }
  }

}


/*

if input can be null? return null


dict = {
            "Key1" : "1",  
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }
        
        , 
        
        {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
        ,
        
        
 new map {
      "Key1" : "1", 
      
  
}

helper(input map, key path ) {
  // base
  if (entry.value is not map) {
    key from key path
    newMap.put(key, value)
  }
  
  for entry in map:
    if entry.value is map
      helper(entry, key path)
    else:
      put
  
}
*/
```
