class solution:
    def nine_box(self, s:str) -> int:
        # step1 count freq
        map = dict()
        for i in range(0, len(s)):
            c = s[i]
            map[c] = map.get(c, 0)+1
        
        # step2 sort map desc
        sortedMap = sorted(map.items(), key=lambda x:x[1], reverse=True)
        
        # step3 arrange the most freq char in first position of each key
        ans = 0
        for idx, item in enumerate(sortedMap):
            if (0 <= idx <= 9):
                ans += 1 * item[1]
            elif (10 <= idx <= 18):
                ans += 2 * item[1]
            else:
                ans += 3 * item[1]
        return ans

s = "abcdefgabc"
obj = solution()
res = obj.nine_box(s)
print(res)