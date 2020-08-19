class Solution:
        
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        ret = []
        pos = [x for x in range(0, m)]
        
        for q in queries:
            curr = pos[q-1]
            ret.append(curr)
            for val in range(0, m):
                if pos[val] < curr:
                    pos[val] += 1
            pos[q-1] = 0
        return ret
        