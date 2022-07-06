class solution:
    def grey(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        rowArr = [0 for _ in range(row)]
        colArr = [0 for _ in range(col)]

        for i in range(row):
            tmp = matrix[i]
            cnt = 0
            for j in range(col):
                if tmp[j] == '1':
                    cnt += 1
                else:
                    cnt -= 1
            rowArr[i] = cnt
        
        for j in range(col):
            cnt = 0
            for i in range(row):
                if (matrix[i][j] == '1'):
                    cnt += 1
                else:
                    cnt -= 1
            colArr[j] = cnt
        
        res = 0
        for i in range(row):
            for j in range(col):
                res = max(res, rowArr[i] + colArr[j])
        return res

obj = solution()
matrix = [
    "1101",
    "0101",
    "1010"
    ]
matrix2 = [
    "1001",
    "0111",
    "0001",
	]
res = obj.grey(matrix)
print(res)