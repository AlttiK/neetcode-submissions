class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        queue = []
        visited = set()

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

        visited.add((0, 0))
        queue.append((0, 0, 1))

        while queue:
            currY, currX, dist = queue.pop(0)
            if currY == len(grid) - 1 and currX == len(grid[0]) - 1:
                return dist
            for direction in directions:
                newLocY = currY + direction[0]
                newLocX = currX + direction[1]
                if 0 <= newLocY < len(grid) and 0 <= newLocX < len(grid[0]) and grid[newLocY][newLocX] == 0 and (newLocY, newLocX) not in visited:
                    queue.append((newLocY, newLocX, dist + 1))
                    visited.add((newLocY, newLocX))

        return -1
