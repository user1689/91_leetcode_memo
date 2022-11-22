```
Root of Number
Many times, we need to re-implement basic functions without using any standard library functions already implemented. For example, when designing a chip that requires very little memory space.

In this question we’ll implement a function root that calculates the n’th root of a number. The function takes a nonnegative number x and a positive integer n, and returns the positive n’th root of x within an error of 0.001 (i.e. suppose the real root is y, then the error is: |y-root(x,n)| and must satisfy |y-root(x,n)| < 0.001).

Don’t be intimidated by the question. While there are many algorithms to calculate roots that require prior knowledge in numerical analysis (some of them are mentioned here), there is also an elementary method which doesn’t require more than guessing-and-checking. Try to think more in terms of the latter.

Make sure your algorithm is efficient, and analyze its time and space complexities.

Examples:

input:  x = 7, n = 3
output: 1.913

input:  x = 9, n = 2
output: 3
Constraints:

[time limit] 5000ms

[input] float x

0 ≤ x
[input] integer n

0 < n
[output] float
```

```java
import java.io.*;
import java.util.*;

class Solution {

  static double root(double x, int n) {
      // your code goes here
      double left = 0.0;
      double right = Math.max(1, x);
      while (right - left >= 1e-3) {
        double mid = left + (right - left) / 2;
        if (Math.pow(mid, n) > x) {
          right = mid;
        } else {
          left = mid;
        }
      }
      return left;
  }

  public static void main(String[] args) {

  }

}
```

```python3
def root(x, n):
  start = 0
  end = max(1,x)
  mid = start + (end -start)/2.0
  while mid - start >= 0.001:
    print(start, end, mid)
    if pow(mid, n) > x:
      end = mid
    else:
      start = mid
    mid = start + (end -start)/2.0
  return mid

print(root(7,3))
"""
x = 0.09, n = 2
ans = 0.3

=> 0-1



n = 3
0 1 2 3 4 5 6 7
s      e
(s, e, m)
(0, 7, 3.5)
(0, 3.5, 1.75)
(1.75, 3.5, 2.625)

(1.75, 2.625, 2.1875)
(1.75, 2.1875, 1.96875)

(1.75, 1.96875, 1.859375)





(0, 7, 3.5)(0, 3.5, 1.75)(1.75, 3.5, 2.625)(1.75, 2.625, 2.1875)(1.75, 2.1875, 1.96875)(1.75, 1.96875, 1.859375)(1.859375, 1.96875, 1.9140625)(1.859375, 1.9140625, 1.88671875)(1.88671875, 1.9140625, 1.900390625)(1.900390625, 1.9140625, 1.9072265625)(1.9072265625, 1.9140625, 1.91064453125)

(1.91064453125, 1.9140625, 1.912353515625)






s = 1.75, e = 3.5, m = 2.625
s = 0, e = 3.5




s = 2.625, e = 3.5 
  
s=1.75, e=3.5, m = 2.625

6.890 

  
3.5/2 = 1.75**2 = 3.0625
m =3.5**2=12.25
 

(0, 7, 3.5)
(0, 3.5, 1.75)
(1.75, 3.5, 2.625)
(1.75, 2.625, 2.1875)


1 2 3 4 5 6 7 8 9
s       e
    m

3**2 =
       
  
1**3  2**3 .... y**n == 9.9


1**3  2**3 .... y**n


1 2 3 4 ... y ..... x
l         m         r
l         r

1 2 3 4 5 ..y......x
s        m         e
    m     e
    s   s e
         4 5 = m = 4.5
            s= 4.5 e = 5
            m = 4.75 
          
          mid = start+end/2.0
  
m**n
pow(m, n) 
"""
```
