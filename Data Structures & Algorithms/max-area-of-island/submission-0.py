class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        area=0
        vis=set()
        def dfs(r,c):
            
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c]==0 or (r,c) in vis:
                return 0
            vis.add((r,c))
            return 1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)
        for r in range(ROWS):
            for c in range(COLS):
                area=max(area,dfs(r,c))
        return area