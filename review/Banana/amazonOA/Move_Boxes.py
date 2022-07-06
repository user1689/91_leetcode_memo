from collections import Counter

class solution:
    def moveBoxes(self, boxes):
        freq = Counter(boxes)    
        ans = 0
        for key, value in freq.items():
            if (value % 3 == 0):
                ans += (value // 3)
            elif (value % 3 == 1):
                ans += ((value-4) // 3)
                ans += 2
            elif (value % 3 == 2):
                ans += ((value-2) // 3)
                ans += 1
        return ans
                    
boxes = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]
boxes2 = [2, 3, 3]
obj = solution()
res = obj.moveBoxes(boxes2)
print(res)