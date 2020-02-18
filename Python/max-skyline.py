class Solution:
    #algo: foreach row, find max height in row, loop over row values, find max in col, (store in hash on first) and add min of maxes to counter
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        colmax = {}
        counter = 0
        for rin in range(0, len(grid)):
            rowmax = max(grid[rin])
            for cid in range(0, len(grid)): #loop over horiz
                if rin == 0:
                    colmax[cid] = grid[rin][cid]
                    for row in grid:
                        if row[cid] > colmax[cid]:
                            colmax[cid] = row[cid]
                counter += (min(rowmax, colmax[cid]) - grid[rin][cid])
        return counter