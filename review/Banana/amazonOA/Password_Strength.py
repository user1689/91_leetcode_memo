class solution:
    def passwordStrength(self, password: str) -> int:

        cnt1 = 0
        cnt2 = 0
        map = {'a', 'e', 'i', 'o', 'u'}
        i, j = 0, 0
        n = len(password)
        ans = 0
        while (i < n):
            if (password[i] in map):
                cnt1+=1
                if (cnt2 > 0):
                    ans+=1
                    cnt1=0
                    cnt2=0
            else: 
                cnt2+=1
                if (cnt1 > 0):
                    ans+=1
                    cnt1=0
                    cnt2=0
            i+=1

        return ans

obj = solution()
password = "thisisbeautiful"
password2 = "applepiepieapple"
res = obj.passwordStrength(password2)
print(res)