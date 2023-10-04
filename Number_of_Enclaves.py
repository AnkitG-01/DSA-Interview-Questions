'''
Number of Enclaves:

You are given an n x m binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Find the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Example 1:

Input:
grid[][] = {{0, 0, 0, 0},
            {1, 0, 1, 0},
            {0, 1, 1, 0},
            {0, 0, 0, 0}}

Output:
3

Explanation:
0 0 0 0
1 0 1 0
0 1 1 0
0 0 0 0

The highlighted cells represents the land cells.

Example 2:

Input:
grid[][] = {{0, 0, 0, 1},
            {0, 1, 1, 0},
            {0, 1, 1, 0},
            {0, 0, 0, 1},
            {0, 1, 1, 0}}

Output:
4

Explanation:
0 0 0 1
0 1 1 0
0 1 1 0
0 0 0 1
0 1 1 0

The highlighted cells represents the land cells.

'''
class Solution:    
    def numberOfEnclaves(self, grid) -> int:
        neighbors=[[0,-1],[-1,0],[1,0],[0,1]]
        rows,cols=len(grid),len(grid[0])
        boundary=[]
        enclave=0

        #Traversing through the array
        for i in range(rows):
            for j in range(cols):
                #Finding the boundary lands and adding to boundary queue
                if grid[i][j] and (i==0 or i==rows-1 or j==0 or j==cols-1):
                    boundary.append([i,j])
                #Counting the non-boundary lands
                if grid[i][j] and 0<i<rows-1 and 0<j<cols-1:
                    enclave+=1
        
        #BFS traversal to find the lands connected to boundary lands
        while boundary:
            x,y=boundary.pop(0)
            if grid[x][y]:
                #Marking the land as visited
                grid[x][y]=0
                #If the land is non-boundary means its connected to a boundary land, so decrement enclave by 1
                if 0<x<rows-1 and 0<y<cols-1:
                    enclave-=1
                #Check if neighbors are land, if yes then add to boundary queue
                for dx,dy in neighbors:
                    nx,ny=x+dx,y+dy
                    if -1<nx<rows and -1<ny<cols and grid[nx][ny]:
                        boundary.append([nx,ny])
        
        return enclave