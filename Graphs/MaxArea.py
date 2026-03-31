class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # t (c) - o(m*n)
        
        if not grid:
            return 0
        
        rows = len (grid)
        cols = len (grid[0])
        
        max_area = 0
        area = 0

        def dfs (cell):
            x,y = cell  
            grid[x][y] = 0
            area = 1
            dirs = [(0,1),(0,-1),(1,0),(-1,0)]
            
            for d in dirs:
                nx = x+d[0]
                ny = y+d[1]                
                if nx < 0 or nx >=rows or ny < 0 or ny >= cols or grid[nx][ny] == 0:
                    continue  
                area += dfs ((nx,ny)) # add the area...this is the key!!
            
            return area
                
        
        
        for i in range (rows):
            for j in range (cols):
                if grid [i][j] == 1:
                    
                    max_area = max (max_area, dfs ((i,j)))
                    # area = 0
        
        return max_area
