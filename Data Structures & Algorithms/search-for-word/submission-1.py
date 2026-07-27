class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        vis=set()
        row,col = len(board), len(board[0])

        def backtrack(r, c, i):
            if i==len(word): return True
            if (r<0 or r>=row or c<0 or c>=col or board[r][c] != word[i] or (r,c) in vis):
                return False
            
            vis.add((r,c))

            res = (
                backtrack(r+1,c,i+1) or backtrack(r-1,c,i+1) or backtrack(r,c+1,i+1) or backtrack(r,c-1,i+1)
            )

            vis.remove((r,c))
            return res

        for r in range(row):
            for c in range(col):
                if backtrack( r,c,0):
                    return True
        return False