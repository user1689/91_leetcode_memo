#### [2. Add Two Numbers](https://leetcode-cn.com/problems/add-two-numbers/)

```java
//Definition for singly-linked list.
public class ListNode {
  	int val;
  	ListNode next;
  	ListNode() {}
  	ListNode(int val) {
      	this.val = val;
    }
  	ListNode(int val, ListNode next) {
      	this.val = val;
      	this.next = next;
    }
}
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode cur3 = dummy;
        int carry = 0;
        ListNode cur1 = l1;
        ListNode cur2 = l2;
        int tmp = 0;
        while (cur1 != null || cur2 != null) {
            if (cur1 == null) {
                tmp = 0 + cur2.val + carry;
            } else if (cur2 == null) {
                tmp = 0 + cur1.val + carry;
            } else {
                tmp = cur1.val + cur2.val + carry;
            }   
            ListNode newNode = new ListNode(tmp % 10);
            cur3.next = newNode;
            cur3 = cur3.next;
            carry = tmp / 10;
            if (cur1 != null) {
                cur1 = cur1.next;
            }
            if (cur2 != null) {
                cur2 = cur2.next;
            }
        }
        if (carry > 0) {
            cur3.next = new ListNode(carry);
        }
        return dummy.next;
        
    }
}
```





#### [82. Remove Duplicates from Sorted List II](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/)

```java
//Definition for singly-linked list.
public class ListNode {
  	int val;
  	ListNode next;
  	ListNode() {}
  	ListNode(int val) {
      	this.val = val;
    }
  	ListNode(int val, ListNode next) {
      	this.val = val;
      	this.next = next;
    }
}
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode dummy = new ListNode(0, head);
        ListNode cur = dummy;
        while (cur.next != null && cur.next.next != null) {
            if (cur.next.val == cur.next.next.val) {
                int x = cur.next.val;
                while (cur.next != null && cur.next.val == x) {
                    cur.next = cur.next.next;
                }
            } else {
                cur = cur.next;
            }
        }
        return dummy.next;
        
    }
}
```



#### [141. Linked List Cycle](https://leetcode-cn.com/problems/linked-list-cycle/)

```java
// Definition for singly-linked list.
public class ListNode {
  	int val;
  	ListNode next;
  	ListNode(int x) {
      this.val = x;
      this.next = null;
    }
}
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (fast == slow) {
                return true;
            }
        }
        return false;

    }
}
```



#### [142. Linked List Cycle II](https://leetcode-cn.com/problems/linked-list-cycle-ii/)

```java
// Definition for singly-linked list.
public class ListNode {
  	int val;
  	ListNode next;
  	ListNode(int x) {
      this.val = x;
      this.next = null;
    }
}
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null) {
            return null;
        }

        ListNode slow = head;
	    ListNode fast = head;
        while (true) {
            if (fast == null || fast.next == null) {
                return null;
            }
            slow  = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                break;
            }
        }
        fast = head;
        while (fast != slow) {
            fast = fast.next;
            slow = slow.next;
        }
        return slow;

    }
}
```



#### [143. Reorder List](https://leetcode-cn.com/problems/reorder-list/)

```java
// Definition for singly-linked list.
public class ListNode {
      int val;
 	    ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  }

public class Solution {
    public void reorderList(ListNode head) {
        // find mid point
        ListNode dummy = new ListNode(-1, head);
        ListNode slow = dummy;
        ListNode fast = dummy;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode cur = slow.next;
        slow.next = null;
        // System.out.println(slow.val);

        // reverse linked list
        ListNode tmp = null;
        while (cur != null) {
            ListNode nxt = cur.next;
            cur.next = tmp;
            tmp = cur;
            cur = nxt;
        }
        ListNode l1 = head;
        ListNode l2 = tmp;

        // merge linked list
        while (l1 != null && l2 != null) {
            ListNode tmp1 = l1.next;
            ListNode tmp2 = l2.next;

            l1.next = l2;
            l1 = tmp1;

            l2.next = tmp1;
            l2 = tmp2;
        }
    }
}
```



#### [144. Binary Tree Preorder Traversal](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)  

```java
// Definition for a binary tree Node.
public class TreeNode {
		int val;
 		TreeNode left;
  	TreeNode right;
  	TreeNode() {}
  	TreeNode(int val) {	this.val = val; }
  	TreeNode(int val, TreeNode left, TreeNode right) {
      this.val = val;
      this.left = left;
      this.right = right;
    }
}
// recursion
public class Solution1 {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> tmp = new ArrayList<>();
        dfs(root, tmp);
        return tmp;
    }
    
    public static void dfs(TreeNode root, List<Integer> path) {
        if (root == null) {
            return;
        } 

        path.add(root.val);
        Solution.dfs(root.left, path);
        Solution.dfs(root.right, path);
    }
}
// iteration
public class Solution2 {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode node = root;
        while (!stack.isEmpty() || node != null) {
            while (node != null) {
                res.add(node.val);
                stack.push(node);
                node = node.left;
            }
            node = stack.pop();
            node = node.right;
        }
        return res;
    }
}
```



#### [145. Binary Tree Postorder Traversal](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/)

```java
// Definition for a binary tree Node.
public class TreeNode {
		int val;
 		TreeNode left;
  	TreeNode right;
  	TreeNode() {}
  	TreeNode(int val) {	this.val = val; }
  	TreeNode(int val, TreeNode left, TreeNode right) {
      this.val = val;
      this.left = left;
      this.right = right;
    }
}
// recursion
public class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        dfs(root, res);
        return res;
    }
    
    public void dfs(TreeNode root, List res) {
        if (root == null) {
            return;
        }
        dfs(root.left, res);
        dfs(root.right, res);
        res.add(root.val);
    }
}
// iteration
public class Solution {
		public List<Integer> postorerTraversal(TreeNode root) {
     		List<Integer> res = new ArrayList<>();
    		Stack<TreeNode> stack = new Stack<>();
     		while (!stack.isEmpty() || root != null) {
        		while (root != null) {
              stack.push(root);
              if (root.left != null) {
              		root = root.left;
              } else {
                	root = root.right;
              }
            }
          	root = stack.pop();
          	res.add(root.val);
          	if (!stack.isEmpty() && stack.peek().left == root) {
            		root = stack.peek().right;
            } else {
            		root = null;
            }
        }
      	return res;
    }
}

```



#### [146. LRU Cache](https://leetcode-cn.com/problems/lru-cache/)

```java
public class LRUCache {
    public class DlinkedNode {
      	public int key;
      	public int value;
      	public DlinkedNode prev;
      	public DlinkedNode next;
      	public DlinkedNode() {}
      	public DlinkedNode(int key, int value) {
          	this.key = key;
        		this.value = value;
        }
    }
		
  	private Map<Integer, DlinkedNode> map = new HashMap<Integer, DlinkedNode>();
  	private int size;
  	private int capacity;
  	private DlinkedNode head;
  	private DlinkedNode tail;
  
    public LRUCache(int capacity) {
				this.size = 0;
      	this.capacity = capacity;
      	this.head = new DlinkedNode();
      	this.tail = new DlinkedNode();
      	head.next = tail;
      	tail.prev = head;
    }
    
    public int get(int key) {
				DlinkedNode node = map.get(key);
      	if (node == null) {
          	return -1;
        }
      	moveToHead(node);
      	return node.value;
    }
    
    public void put(int key, int value) {
				DlinkedNode node = map.get(key);
      	if (node == null) {
        		// 如果 key 不存在，创建一个新的节点
          	DlinkedNode newNode = new DlinkedNode(key, value);
          	map.put(key, newNode);
          	addToHead(newNode);
          	++size;
          	if (size > capacity) {
              	DlinkedNode tail = removeTail();
              	map.remove(tail.key);
              	--size;
            }
        } else {
          	// 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
          	node.value = value;
          	moveToHead(node);
        }
    }
  	
  	public void addToHead(DlinkedNode node) {
      	node.prev = head;
      	node.next = head.next;
      	head.next.prev = node;
      	head.next = node;
    }
  	
  	public void moveToHead(DlinkedNode node) {
      	removeNode(node);
      	addToHead(node);	
    }
  
  	public void removeNode(DlinkedNode node) {
      	node.prev.next = node.next;
      	node.next.prev = node.prev;
    }
  	
  	public DlinkedNode removeTail() {
      	DlinkedNode node = tail.prev;
				removeNode(node);
      	return node;
    }
}
```



#### [147. Insertion Sort List](https://leetcode-cn.com/problems/insertion-sort-list/)

```java
// Definition for singly-linked list.
public class ListNode {
		int val;
		ListNode next;
		ListNode() {}
 		ListNode(int val) { this.val = val; }
  	ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
public class Solution {
    public ListNode insertionSortList(ListNode head) {
        // build dummy
        // it is possible to insert node between dummy and head.
        ListNode dummy = new ListNode(-1, head);
        ListNode last = head;
        ListNode cur = head.next;
        // end loop when cur is null
        while (cur != null) {
            // if last.val <= cur.val, skip the loop
            if (last.val <= cur.val) {
                last = last.next;
                cur = cur.next;
                continue;
            }

            // find node 
            ListNode tmp = dummy;
            while (tmp.next.val <= cur.val) {
                tmp = tmp.next;
            }

            // begin change
            last.next = cur.next;
            cur.next = tmp.next;
            tmp.next = cur;
            cur = last.next;
        }
        return dummy.next;
    }
}
```



#### [148. Sort List](https://leetcode-cn.com/problems/sort-list/)

```java
// Definition for singly-linked list.
public class ListNode {
		int val;
		ListNode next;
		ListNode() {}
 		ListNode(int val) { this.val = val; }
  	ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
public class Solution {
    public ListNode sortList(ListNode head) {
        return mergeSort(head, null);
    }

    public ListNode mergeSort(ListNode head, ListNode tail) {
        if (head == null) {
            return head;
        }
        if (head.next == tail) {
            head.next = null;
            return head;
        }
        ListNode slow = head;
        ListNode fast = head;
        while (fast != tail) {
            slow = slow.next;
            fast = fast.next;
            if (fast != tail) {
                fast = fast.next;
            }
        }
        ListNode mid = slow;
        ListNode lhead = mergeSort(head, mid);
        ListNode rhead = mergeSort(mid, tail);
        return merge(lhead, rhead);
    }

    public ListNode merge(ListNode lhead, ListNode rhead) {
         ListNode dummy = new ListNode(0);
         ListNode cur = dummy;
         ListNode tmp1 = lhead;
         ListNode tmp2 = rhead;
         while (tmp1 != null && tmp2 != null) {
             if (tmp1.val < tmp2.val) {
                 cur.next = tmp1;
                 tmp1 = tmp1.next;
             } else {
                 cur.next = tmp2;
                 tmp2 = tmp2.next;
             }
             cur = cur.next;
         }
         if (tmp1 != null) {
             cur.next = tmp1;
         } else if (tmp2 != null) {
             cur.next = tmp2;
         }
         return dummy.next;
    }

}
```



#### [150. Evaluate Reverse Polish Notation](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/)

```java
class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for (String token : tokens) {
            if (isNumber(token)) {
                stack.push(Integer.parseInt(token));
            } else {
                if (stack.size() >= 2) {
                    int num2 = stack.pop();
                    int num1 = stack.pop();
                    if (token.equals("+")) {
                        stack.push(num1 + num2);
                    } else if (token.equals("-")) {
                        stack.push(num1 - num2);
                    } else if (token.equals("*")) {
                        stack.push(num1 * num2);
                    } else if (token.equals("/")) {
                        stack.push(num1 / num2);
                    }
                }
            }
        }
        return stack.peek();
    }

    public boolean isNumber(String token) {
        return !("+".equals(token) || "-".equals(token) || "*".equals(token) || "/".equals(token));
    }
}
```



#### [151. Reverse Words in a String](https://leetcode-cn.com/problems/reverse-words-in-a-string/)

```java
class Solution {
    public String reverseWords(String s) {
        StringBulider sb = trimSpaces(s);
      	reverse(sb, 0, sb.length() - 1);
      	reverseEachWord(sb);
      	return sb.toString();
    }

    public StringBuilder trimSpaces(String s) {
        int left = 0, right = s.length() - 1;
      	//remove left space
        while (left <= right && s.charAt(left) == ' ') {
            ++left;
        }
				//remove right space
        while (left <= right && s.charAt(right) == ' ') {
            --right;
        }
				// concat the word with only one space
        StringBuilder sb = new StringBuilder();
        while (left <= right) {
            char c = s.charAt(left);

            if (c != ' ') {
                sb.append(c);
            } else if (sb.charAt(sb.length() - 1) != ' ') {
                sb.append(c);
            }

            ++left;
        }
        return sb;
    }
  
    // reverse word in StringBuilder   
    public void reverse(StringBuilder sb, int left, int right) {
      	while (left < right) { 
          	char tmp = sb.charAt(left);
          	sb.setCharAt(left++, sb.charAt(right));
          	sb.setCharAt(right--, tmp);
        }
    }
    // twoPointers
   	public void reverseEachWord(StringBuilder sb) {
      	int start = 0;
      	int end = 0;
      	int n = sb.length();
      	while (start < n) {
          	while (end < n && sb.charAt(end) != ' ') {
              	end += 1;
            }
          	reverse(sb, start, end - 1);
          	start = end + 1;
            end += 1;
        }
    }
    -
}

```



#### [152. Maximum Product Subarray](https://leetcode-cn.com/problems/maximum-product-subarray/)

```java
//Kadane
class Solution {
    public int maxProduct(int[] nums) {
        int[] dp1 = new int[nums.length];
        int[] dp2 = new int[nums.length];
        dp1[0] = nums[0];
        dp2[0] = nums[0];
        int res = nums[0];
        for (int i = 1; i < nums.length; i++) {
            dp1[i] = Math.max(Math.max(dp1[i - 1] * nums[i], dp2[i - 1] * nums[i]), nums[i]);
            dp2[i] = Math.min(Math.min(dp1[i - 1] * nums[i], dp2[i - 1] * nums[i]), nums[i]);
            res = Math.max(res, dp1[i]);
        }
        return res;
    }   
}
```



#### [153. Find Minimum in Rotated Sorted Array](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)

```java
class Solution {
    public int findMin(int[] nums) {
        // find min point 
        int left = 0;
        int right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] >= nums[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return nums[left];
    }
}
```



#### [154. Find Minimum in Rotated Sorted Array II](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/)

```java
class Solution {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else if (nums[mid] < nums[right]) {
                right = mid;
            } else {
                right -= 1;
            }
        } 
        return nums[left];
    }
}
```



#### [155. Min Stack](https://leetcode-cn.com/problems/min-stack/)

```java
class MinStack {

    Stack<Integer> stack1;
    Stack<Integer> stack2;
    public MinStack() {
        this.stack1 = new Stack<>();
        this.stack2 = new Stack<>();
        this.stack2.push(Integer.MAX_VALUE);
    }
    
    public void push(int val) {
        this.stack1.push(val);
        this.stack2.push(Math.min(stack2.peek(), val));
    }
    
    public void pop() {
        this.stack1.pop();
        this.stack2.pop();
    }
    
    public int top() {
        return stack1.peek();
    }
    
    public int getMin() {
        return stack2.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
```



#### [160. Intersection of Two Linked Lists](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/)

```java
//Definition for singly-linked list.
public class ListNode {
  	int val;
  	ListNode next;
  	public ListNode(int x) {
      	val = x;
      	next = null;
    }
}
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode cur1 = headA;
        ListNode cur2 = headB;
        while(cur1 != cur2) {
            if (cur1 != null){
                cur1 = cur1.next;
            } else {
                cur1 = headB;
            }
            if (cur2 != null){
                cur2 = cur2.next;
            } else {
                cur2 = headA;
            }
        }
        return cur1;
    }

//reference: https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/xiang-jiao-lian-biao-by-leetcode-solutio-a8jn/
}
```



#### [162. Find Peak Element](https://leetcode-cn.com/problems/find-peak-element/)

```java
class Solution {
    public int findPeakElement(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if ((nums[mid] > nums[mid + 1])){
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}
```



#### [165. Compare Version Numbers](https://leetcode-cn.com/problems/compare-version-numbers/)

```java
class Solution {
    public int compareVersion(String version1, String version2) {
        int i = 0;
        int j = 0;
        while (i < version1.length() || j < version2.length()) {
            int num1 = 0;
            while (i < version1.length() && version1.charAt(i) != '.') {
                num1 = num1 * 10 + (version1.charAt(i) - '0');
                i += 1;
            }
            i += 1;
            int num2 = 0;
            while (j < version2.length() && version2.charAt(j) != '.') {
                num2 = num2 * 10 + (version2.charAt(j) - '0');
                j += 1;
            }
            j += 1;
            if (num1 != num2) {
                return num1 > num2 ? 1 : -1;
            }
        }
        return 0;
    }
}
```



#### [166. Fraction to Recurring Decimal](https://leetcode-cn.com/problems/fraction-to-recurring-decimal/)

```java
class Solution {
  	public String fractionToDecimal(int numerator, int denominator) {
    		long a = numerator;
      	long b = demoninator;
      	if (a % b == 0) {
          return String.valueOf(a / b);
        }
      	StringBuilder sb = new StringBuilder();
      	if (a * b < 0) {
          	sb.append('-');
        }
      	a = Math.abs(a);
      	b = Math.abs(b);
      	sb.append(String.valueOf(a / b) + ".");
      	Map<Long, Integer> map = new HashMap<>();
      	a = a % b;
      	while (a != 0) {
          	map.put(a, sb.length());
          	a *= 10;
            sb.append(a / b);
          	a %= b;
          	if (map.containsKey(a)) {
              	int u = map.get(a);
              	return String.format("%s(%s)", sb.subString(0, u), sb.subString(u));
            }
        }
      	return sb.toString();
    }
}
```



#### [167. Two Sum II - Input Array Is Sorted](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)

```java
//twoPointers
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0;
        int j = numbers.length - 1;
        while (i < j) {
            if (numbers[i] + numbers[j] < target) {
                i += 1;
            } else if (numbers[i] + numbers[j] > target) {
                j -= 1;
            } else {
                return new int[]{i + 1, j + 1};
            }
        }
        return new int[]{i + 1, j + 1};
    }
}
//binarySearch
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            int left = i + 1;
            int right = nums.length - 1;
            while (left <= right) {
                int mid = (left + (right - left) / 2);
                if (nums[mid] + nums[i] > target) {
                    right = mid - 1;
                } else if (nums[mid] + nums[i] < target) {
                    left = mid + 1;
                } else if (nums[mid] + nums[i] == target) {
                    return new int[]{i + 1, mid + 1};
                }
            }
        }
        return new int[]{-1, -1};
    }
}
```



#### [168. Excel Sheet Column Title](https://leetcode-cn.com/problems/excel-sheet-column-title/)

```java
class Solution {
    public String convertToTitle(int columnNumber) {
        StringBuilder sb = new StringBuilder();
        while (columnNumber > 0) {
            columnNumber -= 1;
            sb.append((char)(columnNumber % 26 + 'A'));
            columnNumber = columnNumber / 26;
        } 
        sb.reverse();
        return sb.toString();
    }
}
```



#### [169. Majority Element](https://leetcode-cn.com/problems/majority-element/)

```java
class Solution {
    public int majorityElement(int[] nums) {
        int element = 0;
        int cnt = 0;
        for (int num : nums) {
            if (cnt > 0 && num == element) {
                cnt += 1;
            } else if (cnt == 0){
                element = num;
                cnt = 1;
            } else {
                cnt -= 1;   
            }
        }
        return element;
    }
}
```



#### [171. Excel Sheet Column Number](https://leetcode-cn.com/problems/excel-sheet-column-number/)

```java
class Solution {
  	public int titleToNumber(String columnTitle) {
      	char[] cs = columnTitle.toCharArray();
      	int n = cs.length;
      	int num = 0;
      	for (int i = 0; i < n; i++) {
          	num = num * 26 + (cs[i] - 'A' + 1);
        }
      	return num;
    }
}
```



#### [172. Factorial Trailing Zeroes](https://leetcode-cn.com/problems/factorial-trailing-zeroes/)

```java
class Solution {
    public int trailingZeroes(int n) {
        int cnt = 0;
        while (n != 0) {
            int tmp = n / 5;
            cnt += tmp;
            n = tmp;
        }
        return cnt;
    }
}
```



#### [173. Binary Search Tree Iterator](https://leetcode-cn.com/problems/binary-search-tree-iterator/)

```java
//Definition for a binary tree node.
public class TreeNode {
		int val;
  	TreeNode left;
  	TreeNode right;
  	TreeNode () {}
  	TreeNode (int val) {
      	this.val = val;
    }
  	TreeNode (int val, TreeNode left, TreeNode right) {
      	this.val = val;
      	this.left = left;
      	this.right = right;
    }
}
class BSTIterator {

    Stack<TreeNode> stack;

    public BSTIterator(TreeNode root) {
        this.stack = new Stack<>();
        while (root != null) {
            stack.push(root);
            root = root.left;
        }
    }
    
    public int next() {
        TreeNode tmp = stack.peek();
        TreeNode cur = tmp.right;
        stack.pop();
        while (cur != null) {
            stack.push(cur);
            cur = cur.left;
        }
        return tmp.val;
    }
    
    public boolean hasNext() {
        return !stack.isEmpty();
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
```



#### Test

```java
class Car {
  public int price;
  public String name;
  
  public Car(int price, String name) {
    	this.price = price;
    	this.name = name;
  }
}
class solution {
  	public static void main(String[] args) {
      	Car car1 = new Car(128, "qq");
      	Car car2 = new Car(200, "aa");
        Car car3 = new Car(128, "qq");
      	Car car4 = new Car(392, "zz");
        Car car5 = new Car(128, "qq");
      	Car car6 = new Car(193, "kk");
      	Car[] cars = new Car[]{car1, car2, car3, car3, car4, car5, car6};
      	Comparator<Car> cmp = new Comparator<Car>(){
          	@Override
          	public int compare(Car c1, Car c2) {
              	return c1.price - c2.price;
            }
        };
      
      	Comparator<Car> cmp2 = (c1, c2) -> (c1.name.compareTo(c2.name));
      	Arrays.sort(cars, cmp2);
      	for (Car c : cars) {
          	System.out.println(c.name);
        }
    }
}
```





#### findMid

```python
class Solution:
	def findMid(self, root):
      slow = root
      fast = root
      while (fast.next and fast.next.next):
          slow = slow.next
          fast = fast.next.next
      return slow
```

