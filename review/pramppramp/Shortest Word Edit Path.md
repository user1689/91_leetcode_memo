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
