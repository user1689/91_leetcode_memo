# Array Index & Element Equality
____
## Question
Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch that returns the lowest index i for which arr[i] == i. Return -1 if there is no such index. Analyze the time and space complexities of your solution and explain its correctness.

Examples:

input: arr = [-8,0,2,5]
output: 2 # since arr[2] == 2

input: arr = [-1,0,3,6]
output: -1 # since no index in arr satisfies arr[i] == i.

Constraints:

[time limit] 5000ms

[input] array.integer arr

1 ≤ arr.length ≤ 100
[output] integer

## My Solution
____
```python3
def index_equals_value_search(arr):
  l = 0
  r = len(arr) - 1
  while (l <= r):
    mid = l + (r - l) // 2
    if (arr[mid] == mid):
      return mid
    elif (arr[mid] > mid):
      r = mid - 1
    else:
      l = mid + 1
  return -1

  
'''
0  1 2 3 seq1
-1 0 1 x seq2
     i
number at index i is smaller than index i, so seq2 wants to becomes as bigger as possible in the range of [0, i-1], so that it can catch up the index i-1
we wants to make this two sequence meets at range of [0, i-1], so we try to 
give a maximum number seq2 can get in the previous is 0, cause input is sorted
give a minimum index seq1 can get in the previous is 1, cause index is sorted, and gap is 1
obiviously, index 1 doesn't euqals to number 1 do it again..
finllay, we found that it is impossible to catch up at the rang of [0, i-1], so we give up this part.

let's discuss right part
number at index i is smaller than index i, so seq2 wants to becomes as bigger as possible in the range of [i+1, n-1]
we do the same things again
because seq2 is sorted, so x should starting from 2, but now I gonna give a suitable number seq2 here, let suppose x = 3
we want seq2 to catch up seq1 in the range of [i+1, n-1], so give a minimum index seq1 can get which is 3, cause index is sorted, and gap is 1

if x =3, 3 is our answer, we can say that answer may appears in the right part which is range of [i+1, n-1], so this when considering this two sequence, we can say they have monotonicity

if a sequence has monotonicity, we can apply binary search to it


eg1:

  0. 1. 2. 3
[-8, 0, 2, 5]
  l. m.    r
    idx > num, search in right part
 
eg2:
  0. 1. 2. 3
[-1, 0, 3, 6]
  l. m.    r
    idx > num, search in right part
    
eg3:
  
  0  1  2  3  4
[-1, 1, 3, 4, 5]
  l.    m.    r
    idx < num, search in the left part


'''


```
