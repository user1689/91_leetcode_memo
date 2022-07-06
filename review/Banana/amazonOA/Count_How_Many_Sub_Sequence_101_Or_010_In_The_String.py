class solution:
    def countSubsequence101010(self, s:str) -> int:

        '''
        010
        101
        '''

        def dfs(i, j, tmp):
            if (i < 0 and j < 0):
                return 1
            if (j < 0):
                return 1
            if (i < 0):
                return 0
            
            res = 0
            if (s[i] == tmp[j]):
                res += dfs(i-1, j, tmp)
                res += dfs(i-1, j-1, tmp)
            else:
                res += dfs(i-1, j, tmp)

            return res

        n = len(s)
        tmp1 = "010"
        tmp2 = "101"
        a = dfs(n-1, len(tmp1)-1, tmp1) 
        b = dfs(n-1, len(tmp2)-1, tmp2)
        return a + b


obj = solution()
res = obj.countSubsequence101010("01001")
print(res)