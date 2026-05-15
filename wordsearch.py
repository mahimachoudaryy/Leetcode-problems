class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row,col,ind,directions,board):
            if ind==len(word):
                return True
            for r,c in directions:
                nr=row+r
                nc=col+c
                if (nr>=0 and nr<m and nc>=0 and nc<n):
                    if(board[nr][nc]==word[ind]):
                        board[nr][nc]='.'
                        if(backtrack(nr,nc,ind+1,directions,board)):
                            return True 
                        board[nr][nc] = word[ind]
            return False 
        directions=[[1,0],[0,1],[0,-1],[-1,0]]
        m=len(board)  
        n=len(board[0])
        for row in range(0,m):
            for col in range(0,n):
                if(board[row][col] == word[0]):
                    board[row][col] = '.'
                    if(backtrack(row,col,1,directions,board)):
                        return True
                    board[row][col] = word[0] 
        return False
