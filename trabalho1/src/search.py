import time
from collections import deque
import heapq
from typing import List, Tuple, Callable, Dict, Optional

try:
    from .maze import Maze
    from .heuristics import h_manhattan
except ImportError:
    from maze import Maze
    from heuristics import h_manhattan

Pos = Tuple[int, int]


def reconstruct_path(came_from: Dict[Pos, Pos], start: Pos, goal: Pos) -> List[Pos]:
    current = goal
    path = []
    if goal not in came_from:
        return []
    while current is not None:
        path.append(current)
        current = came_from.get(current)
    path.reverse()
    return path


def bfs(maze: Maze) -> Optional[Dict]:
    start_time = time.time()

    start_node = maze.start
    goal_node = maze.goal

    queue = deque([start_node])
    came_from = {start_node: None}

    nodes_expanded = 0
    max_memory = 1

    while queue:
        nodes_expanded += 1
        current = queue.popleft()

        if current == goal_node:
            path = reconstruct_path(came_from, start_node, goal_node)
            end_time = time.time()
            return {
                "path": path,
                "cost": len(path) - 1,
                "nodes_expanded": nodes_expanded,
                "max_memory": max_memory,
                "runtime": end_time - start_time,
            }

        for neighbor in maze.get_neighbors(current):
            if neighbor not in came_from:
                came_from[neighbor] = current
                queue.append(neighbor)
                max_memory = max(max_memory, len(queue) + len(came_from))

    return None


def dfs(maze: Maze) -> Optional[Dict]:
    start_time = time.time()

    start_node = maze.start
    goal_node = maze.goal

    stack = [start_node]
    came_from = {start_node: None}

    nodes_expanded = 0
    max_memory = 1

    while stack:
        nodes_expanded += 1
        current = stack.pop()

        if current == goal_node:
            path = reconstruct_path(came_from, start_node, goal_node)
            end_time = time.time()
            return {
                "path": path,
                "cost": len(path) - 1,
                "nodes_expanded": nodes_expanded,
                "max_memory": max_memory,
                "runtime": end_time - start_time,
            }

        for neighbor in maze.get_neighbors(current):
            if neighbor not in came_from:
                came_from[neighbor] = current
                stack.append(neighbor)
                max_memory = max(max_memory, len(stack) + len(came_from))

    return None


def greedy_search(maze: Maze, heuristic: Callable[[Pos, Pos], float]) -> Optional[Dict]:
    start_time = time.time()

    start_node = maze.start
    goal_node = maze.goal

    priority_queue = [(0, start_node)]
    came_from = {start_node: None}

    nodes_expanded = 0
    max_memory = 1

    while priority_queue:
        nodes_expanded += 1
        _, current = heapq.heappop(priority_queue)

        if current == goal_node:
            path = reconstruct_path(came_from, start_node, goal_node)
            end_time = time.time()
            return {
                "path": path,
                "cost": len(path) - 1,
                "nodes_expanded": nodes_expanded,
                "max_memory": max_memory,
                "runtime": end_time - start_time,
            }

        for neighbor in maze.get_neighbors(current):
            if neighbor not in came_from:
                priority = heuristic(neighbor, goal_node)
                heapq.heappush(priority_queue, (priority, neighbor))
                came_from[neighbor] = current
                max_memory = max(max_memory, len(priority_queue) + len(came_from))

    return None


def a_star(maze: Maze, heuristic: Callable[[Pos, Pos], float]) -> Optional[Dict]:
    start_time = time.time()

    start_node = maze.start
    goal_node = maze.goal

    priority_queue = [(0, start_node)]
    came_from = {start_node: None}
    cost_so_far = {start_node: 0}

    nodes_expanded = 0
    max_memory = 1

    while priority_queue:
        nodes_expanded += 1
        _, current = heapq.heappop(priority_queue)

        if current == goal_node:
            path = reconstruct_path(came_from, start_node, goal_node)
            end_time = time.time()
            return {
                "path": path,
                "cost": cost_so_far[goal_node],
                "nodes_expanded": nodes_expanded,
                "max_memory": max_memory,
                "runtime": end_time - start_time,
            }

        for neighbor in maze.get_neighbors(current):
            new_cost = cost_so_far[current] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal_node)
                heapq.heappush(priority_queue, (priority, neighbor))
                came_from[neighbor] = current
                max_memory = max(max_memory, len(priority_queue) + len(came_from))

    return None