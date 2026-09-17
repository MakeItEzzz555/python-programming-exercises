from collections import deque

def load_map(filename):
    grid = []
    with open(filename, 'r') as f:
        for line in f:
            grid.append(list(line.strip()))
    return grid

def is_valid(grid, x, y):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] == '0'

def bfs(grid, start, end):
    queue = deque()
    queue.append(start)
    visited = set()
    visited.add(start)
    parent = {}

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        x, y = queue.popleft()

        if (x, y) == end:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            return path[::-1]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(grid, nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
                queue.append((nx, ny))

    return None

def main():
    filename = input("Enter map filename: ")
    grid = load_map(filename)

    while True:
        xs, ys = map(int, input("Enter Start-Point (Xs Ys): ").split())
        if is_valid(grid, xs, ys):
            break
        print("Invalid start point. Try again.")

    while True:
        xe, ye = map(int, input("Enter End-Point (Xe Ye): ").split())
        if is_valid(grid, xe, ye):
            break
        print("Invalid end point. Try again.")

    path = bfs(grid, (xs, ys), (xe, ye))

    if path:
        print("\nShortest Path:")
        for p in path:
            print(p)
        print(f"\nPath length: {len(path)-1} steps")

        # Optional visualization
        for x, y in path:
            grid[y][x] = '*'
        print("\nMap with path:")
        for row in grid:
            print("".join(row))
    else:
        print("No path exists between the given points.")

if __name__ == "__main__":
    main()
