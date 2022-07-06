class solution:
    def commonPrefix(self, inputs:str):
        l, r = 0, 0
        n = len(inputs)
        z = [0] * n
        for i in range(1, n):
            if (z[i - l] < r - i + 1):
                z[i] = z[i - l]
            else:
                z[i] = max(0, r - i + 1)
                while (i + z[i] < n and inputs[z[i]] == inputs[i + z[i]]):
                    z[i] += 1
                l = i
                r = i + z[i] - 1
        return sum(z) + n

obj = solution()
res = obj.commonPrefix("abcabcd")
print(res)

