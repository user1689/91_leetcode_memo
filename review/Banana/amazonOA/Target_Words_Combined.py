class solution:
    def Target_Words_Combined(self, s:str, t:str) -> int:
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        for i in range(len(s)):
            cnt1[ord(s[i]) - ord('a')] += 1
        for j in range(len(t)):
            cnt2[ord(t[j]) - ord('a')] += 1
        ans = 0x3f3f3f3f
        for k in range(26):
            if (cnt2[k] != 0 and cnt1[k] != 0):
                ans = min(ans, cnt1[k] // cnt2[k])
        return ans
        
obj = solution()
s = "mononom"
t = "mon"
obj.Target_Words_Combined(s, t)