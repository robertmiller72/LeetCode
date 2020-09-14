#554ms

class Solution:
    import collections
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        infi = 2147483647
        def bfs(grid, start):
            width = len(grid[0])
            height = len(grid)
            deque = collections.deque([[start]])
            seen = set([start])
            while deque:
                path = deque.popleft()
                x, y = path[-1]
                if grid[x][y] == 0:
                    return len(path) - 1
                for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    if 0 <= x2 < height and 0 <= y2 < width and (x2, y2) not in seen and grid[x2][y2] != -1:
                        deque.append(path + [(x2, y2)])
                        seen.add((x2, y2))
            return infi
                        
        for x in range(len(rooms)):
            for y in range(len(rooms[x])):
                if rooms[x][y] == infi:
                    rooms[x][y] = bfs(rooms, (x,y))
                    
        return rooms