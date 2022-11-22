## Unsorted

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
