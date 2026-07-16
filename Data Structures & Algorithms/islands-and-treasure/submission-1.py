
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS,COLS=len(grid),len(grid[0])
        vis=set()
        q=deque()
        
        
        
        def addCell(r,c):
            if min(r,c)<0 or r==ROWS or c==COLS or (r,c) in vis or grid[r][c]==-1:
                return
            vis.add((r,c))
            q.append([r,c])
        dist=0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    q.append([r,c])
                    vis.add((r,c))
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dist
                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c+1)
                addCell(r,c-1)
            dist+=1
