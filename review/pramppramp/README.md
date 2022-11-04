Unsorted

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



 ```java
import java.util.*;
class Question01 {
    public static void main(String[] args) {
        LinkedList<Integer> stack1 = new LinkedList<>();
        stack1.push(1);
        stack1.push(2);
        stack1.push(3);
        System.out.println(stack1.get(0)); // 3
        
        LinkedList<Integer> stack2 = new LinkedList<>();
        stack2.offerLast(1);
        stack2.offerLast(2);
        stack2.offerLast(3);
        System.out.println(stack2.get(0)); // 1
    }
}
```
