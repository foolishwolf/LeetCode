class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                if i != 0 and grid[i-1][j] == 0 or i == 0:
                    perimeter += 1
                if i != len(grid)-1 and grid [i+1][j] == 0 or i == len(grid)-1:
                    perimeter += 1
                if j != 0 and grid[i][j-1] == 0 or j == 0:
                    perimeter += 1
                if j != len(grid[i])-1 and grid[i][j+1] == 0 or j == len(grid[i])-1:
                    perimeter += 1
        return perimeter