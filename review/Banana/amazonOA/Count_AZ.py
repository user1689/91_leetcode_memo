import bisect
from typing import List

class solution:
    def countAZ(self, s:str) -> int:
        '''
        要么A加在最前面
        要么Z加在最后面

        A + frq(substring)
        frq(substring) + Z
        '''

        posA = []
        posZ = []
        for i in range(0, len(s)):
            if (s[i] == 'A'):
                posA.append(i)
            elif (s[i] == 'Z'):
                posZ.append(i)
        cnt = 0
        for idx in posA:
            dis = bisect.bisect_left(posZ, idx)
            cnt += (len(posZ) - dis)
        
        return cnt + len(posA) if cnt + len(posA) > cnt + len(posZ) else cnt + len(posZ)


obj = solution()
res = obj.countAZ("KAZ")
print(res)