import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    rows, cols = grid.shape
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    cost_so_far = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            break

        neighbors = [(0,1),(1,0),(0,-1),(-1,0)]

        for dx, dy in neighbors:
            next_node = (current[0] + dx, current[1] + dy)

            if 0 <= next_node[0] < rows and 0 <= next_node[1] < cols:
                if grid[next_node[0]][next_node[1]] == 1:
                    continue

                new_cost = cost_so_far[current] + 1

                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + heuristic(goal, next_node)
                    heapq.heappush(open_list, (priority, next_node))
                    came_from[next_node] = current

    # reconstruct path
    path = []
    current = goal

    while current != start:
        path.append(current)
        current = came_from.get(current, start)

    path.append(start)
    path.reverse()

    return path