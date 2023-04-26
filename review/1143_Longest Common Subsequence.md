question:  
https://leetcode.cn/problems/longest-common-subsequence/

solution:
```javascript
/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function(text1, text2) {
    
    const n = text1.length;
    const m = text2.length;
    const memo = Array(n).fill(-1).map(() => Array(m).fill(-1));
    
    const dfs = function(i, j) {
        if (i == n || j == m) { 
            // console.log("end");
            return 0;
        }
        if (memo[i][j] != -1) return memo[i][j];
        
        let res = 0;
        if (text1.charAt(i) === text2.charAt(j)) {
            res = dfs(i+1, j+1) + 1;
        } else {
            res = Math.max(dfs(i+1, j), dfs(i, j+1));
        }
        memo[i][j] = res;
        return res;
         
    }

    return dfs(0, 0);
};
```
