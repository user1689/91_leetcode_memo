## question
```
given a string s of lowercase english characters the following operations can be performed on it any number of times. 

choose three consecutive char, s[i], s[i+1], s[i+2] where such that s[i] = s[i+1] and s[i+1] != s[i+2], replace s[i+2] with s[i], find maximum number of operations that can be applied to s.

example 1
consider s = accept

step1  change `e` to `c`, so after operation we got `acccpt`
step2 change `p` to `c`, so after operation we got `acccct`
step3 change `t` to `c`, so after operation we got `accccc`
so answer is 3

example2
consider s = aaabbc

step1  change `c` to `b`, so after operation we got `aaabbb`
step2 change `b` to `a`, so after operation we got `aaaabb`
step3 change `b` to `a`, so after operation we got `aaaaab`
step3 change `b` to `a`, so after operation we got `aaaaaa`
so answer is 4
```

```python3
# def find_max_operations(s):
#     def helper(s):
#         max_ops = 0
#         n = len(s)

#         # Base case: If the length of the string is less than 3, return 0 operations
#         if n < 3:
#             return 0

#         # Recursive case: Try all possible operations
#         for i in range(n - 2):
#             if s[i] == s[i + 1] and s[i + 1] != s[i + 2]:
#                 new_s = s[:i + 2] + s[i] + s[i + 3:]
#                 max_ops = max(max_ops, 1 + helper(new_s))
#         return max_ops
#     return helper(s)

def find_max_operations(s):
    memo = {}  # Memoization dictionary to store computed results

    def helper(s):
        if s in memo:
            return memo[s]

        max_ops = 0
        n = len(s)

        # Base case: If the length of the string is less than 3, return 0 operations
        if n < 3:
            memo[s] = 0
            return 0

        # Recursive case: Try all possible operations
        for i in range(n - 2):
            if s[i] == s[i + 1] and s[i + 1] != s[i + 2]:
                new_s = s[:i + 2] + s[i] + s[i + 3:]
                max_ops = max(max_ops, 1 + helper(new_s))

        memo[s] = max_ops
        return max_ops

    return helper(s)

# Test examples
print(find_max_operations("accept"))  # Output: 3
print(find_max_operations("aaabbc"))  # Output: 4
print(find_max_operations("acceptccept"))  # 6
print(find_max_operations("afz")) # 0
print(find_max_operations("accxck")) # 2
print(find_max_operations("accxcc")) # 1
print(find_max_operations("aabbc")) # 4
```
 
