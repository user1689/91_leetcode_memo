from typing import List

class solution:
    def find_data_locations(self, locations:List[int], movedFrom:List[int], movedTo:List[int]) -> int:   
        s = set(locations)
        for f, t in zip(movedFrom, movedTo):
            if (f != t):
                s.remove(f)
                s.add(t)
        return sorted(s)
  	    # return list(s).sort()
 
obj = solution()
locations = [1,7,6,8]
movedFrom = [1,7,2]
movedTo = [2,9,5]
res = obj.find_data_locations(locations, movedFrom, movedTo)
print(res)