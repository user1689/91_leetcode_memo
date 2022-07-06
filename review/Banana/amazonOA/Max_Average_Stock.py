from typing import List

class solution:
    def max_average_stock(self, arr:List[int], k:int) -> int:   
        # step1 calculate prefix sum
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(0, n):
            prefix[i+1] = prefix[i] + arr[i]
        
        # step2 using two pointers and set to maintain max value
        seen = set()
        left = 0
        right = 0
        ans = -1
        while (left < n and right < n):
            while (right == n and (right - left > k)):
                left+=1

            while (left < n and right < n and arr[right] in seen):
                seen.remove(arr[left])
                left+=1

            seen.add(arr[right])
            right+=1
            
            if ((right - left) == k):
                ans = max(ans, prefix[right] - prefix[left])
                if (left < n):
                    seen.remove(arr[left])
                    left+=1

        # step3 calculate last interval
        if (ans != -1):
            tmp = sum(seen)
            ans = max(ans, tmp)    
            
        return ans

arr = [1,2,7,7,4,4,6,8,9]
obj = solution()
k = 3
res = obj.max_average_stock(arr, k)
print(res)