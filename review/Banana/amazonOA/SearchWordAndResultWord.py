class solution:
    def searchWordAndResultWord(self, searchWord, resultWord) -> int:
        i, j = 0, 0
        n = len(resultWord)
        m = len(searchWord)
        while (i < m and j < n):
            if (i <  m and j < n and searchWord[i] == resultWord[j]):
                j+=1
            i+=1
        return n - j
      
obj = solution()
searchWord = "cd"
resultWord = "cdefgzz"
res = obj.searchWordAndResultWord(searchWord, resultWord)
print(res)