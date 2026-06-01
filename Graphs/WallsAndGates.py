# "My first thought is multi-source BFS. We need the shortest distance from each empty room to the nearest gate. Since the grid is unweighted and there can be multiple gates, I'll enqueue all gates initially and perform BFS outward. BFS guarantees that cells are visited in increasing distance order, so the first time we reach a room we've found its minimum distance. This gives O(mn) time and O(mn) space." 

# If the interviewer asks about DFS: "DFS can be made to work by propagating distances from each gate and revisiting cells when a shorter distance is found, but it doesn't naturally produce shortest paths and may revisit cells many times. Multi-source BFS is both cleaner and more efficient."

from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return rooms
        
        rows = len (rooms)
        cols = len (rooms[0])

        queue = deque ([])
        for i in range (rows):
            for j in range (cols):
                if rooms [i][j] == 0:
                    queue.append ((i,j))

        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        while queue:
            cell = queue.popleft()
            cell_x = cell[0]
            cell_y = cell[1]

            for d in dirs:
                new_x = cell_x + d[0]
                new_y = cell_y + d[1]
                if new_x >=0 and new_x < rows and new_y >=0 and new_y < cols and rooms [new_x][new_y] == 2147483647:
                    rooms[new_x][new_y] = rooms[cell_x][cell_y] + 1
                    queue.append ((new_x,new_y)) 
