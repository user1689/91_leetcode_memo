## 题目
https://leetcode-cn.com/problems/reverse-words-in-a-string/

## 思路
imitation

## Java
```java
class Solution {
    public String reverseWords(String s) {
        int start = 0;
        int n = s.length();
        int end = n - 1;
        char[] ss = s.toCharArray();
        // remove space
        while (start <= end && ss[start] == ' ') {
            start++;
        }
        while (start <= end && ss[end] == ' ') {
            end--;
        }
        
        swap(start, end, ss);
        
        int i = start, j = start;
        int mark = start;
        while (j <= end) {
            
            if (ss[j] != ' ') {
                ss[mark++] = ss[j];
            }
            
            if (j == end || ss[j] == ' ') {
                swap(i, mark-1, ss);
                
                if (j == end) {
                    break;
                }
                
                ss[mark++] = ' ';
                i = mark;
                
                while (ss[j] == ' ') {
                    j++;
                }
                
                j--;
            }      
            
            j++;
        }
        return new String(ss, start, mark - start);

    }
    void swap(int i, int j, char[] ss) {
        while (i < j) {
            char tmp = ss[i];
            ss[i] = ss[j];
            ss[j] = tmp;
            i++;
            j--;
        }
        
    }
}
```

```java
class Solution {
    public String reverseWords(String s) {
        // step1 trim leading space and tailing space
        int i = 0, j = s.length() - 1;
        while (s.charAt(i) == ' ') {
            i++;
        }
        while (s.charAt(j) == ' ') {
            j--;
        }
        
        // step2 insert into deque word by word
        StringBuilder sb = new StringBuilder();
        Deque<String> deque = new ArrayDeque<>();
        
        while (i <= j) {
            char c = s.charAt(i);
            if (sb.length() != 0 && c == ' ') {
                deque.offerFirst(sb.toString());
                sb = new StringBuilder();
            } else if (c != ' ') {
                sb.append(s.charAt(i));
            }
            i++;
        }
        deque.offerFirst(sb.toString());
        
        // step3 construct ans
        return String.join(" ", deque);
    }
}
```

## python3
```python3
class Solution:
    def reverseWords(self, s: str) -> str:
        def trim_(s):
            left, right = 0, len(s) - 1
            while left <= right and s[left] == ' ':
                left += 1
            while right <= right and s[right] == ' ':
                right -= 1
            
            output = []
            while left <= right:
                if s[left] != ' ':
                    output.append(s[left])
                # 细节！！！
                # s[left] == ' '
                # 当output中最后一个字符不为空时候加入空格，如果有就不加入
                elif output[-1] != ' ':
                    output.append(s[left])
                left += 1

            return output

        def reverse(l, left, right):
            while left <= right:
                l[left], l[right] = l[right], l[left]
                left += 1
                right -= 1
        
        def reverse_each_words(l):
            n = len(l)
            start = end = 0
            while end < n:
                # 循环至单词的末尾
                while end < n and l[end] != ' ':
                    end += 1
                # 翻转单词
                reverse(l, start, end - 1)
                # 更新start，去找下一个单词
                start = end + 1
                end += 1

        l = trim_(s)
        reverse(l, 0, len(l) - 1)
        reverse_each_words(l)

        return ''.join(l)

```

## 复杂度分析
* time n
* space n

## 相关题目
1. 待补充
