
```
We have a binary search tree and a number N. Our task is to find the greatest number in the binary search tree that is less than or equal to N. Print the value of the element if it exists otherwise print -1.  
ref: https://practice.geeksforgeeks.org/problems/closest-neighbor-in-bst/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
```

```Java
    int findLargestSmallerKey(int num) {
      // your code goes here 
      Node ans = recursion(root, num);
      return ans == null ? -1 : ans.key; 
      
      /*
          
          step1 define a global value as previous
          step2 doing inorder traverse of BST, and store current to global value previous
          step3 when the current value is bigger than or equal to given value, the previous one is answer
          
          
          prev = 14, cur = 20 bigger than 17
                  
          20 > 17
          9 < 17, 
          12 < 17
                    
              
          num = 17
              
                
              20
            /  
           null

         
         cur = 14, 14 < 17
         18 > 17
         14
          
            20
           /  \
          14  25
         /  \
        12  18
        
        
        cur = 14
        and cause right part is null, ans is 14
           
           20
          /  \
         17  25
        /  \
       14*  18  
          
             
              20
                \
                 25
             
                   
                    
               9     
             /  \      
            5   12 
               /  \  cur
              11  14
                    \
                     null
            
                
                cur
               9
              /
            5
            
           given = 17
                  
                    ans 
                  16
                 /  \
                9   25
             
           
                    ans1
                  20
                /   \ 
               9    25
             /  \      
            5   12
               /  \ ans2
              11  14
            
             
      */
    }
    
    /*
    
     root = 14
        recursion(16)
            root = 16   
              recursion(null) 
                root = null
    
            20
           /  \
          14  25
         /  \
        12  16*
        
      root = 20 
       recursion(20)
          recursion(null) => null
          
            20
           
        
    */    
    
    Node recursion(Node root, int num) { // recursion(null) -> null -> recursion(16)
      // base
      if (root == null) return null;
      
      /*
          compare value at root with give value
      */
      if (root.key >= num) {
        // search in left part
        return recursion(root.left, num);
      } else {
        // search in right part
           // it is possible that root is a ans, but we are sure about that
           Node answerFromRightPart = recursion(root.right, num);
           if (answerFromRightPart == null) return root; // answerFromRightPart = null, return root = 16 
           else return answerFromRightPart;
      }
      
    }
```
