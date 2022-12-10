
import heapq
from Helper_functions import helper_functions as helpers
from collections import deque
from Game_configurations import config


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def dfs(board, start, goal):
    stack = [start]
    visited = set()
    full_path = []

    while stack:
        current = stack.pop()
        full_path.append(current)
        if current == goal:
            return full_path
        for direction in ["up", "right", "down", "left"]:  # Other orders are fine too.
            row_offset, col_offset = config.offsets[direction]
            neighbour = (current[0] + row_offset, current[1] + col_offset)
            if helpers.is_legal_pos(board, neighbour) and neighbour not in visited:
                stack.append(neighbour)
                visited.add(neighbour)


def bfs(board, start, goal):
    queue = deque()
    queue.append(start)
    visited = set()
    full_path = []

    while queue:
        current = queue.popleft()
        full_path.append(current)
        if current == goal:
            return full_path
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = config.offsets[direction]
            neighbour = (current[0] + row_offset, current[1] + col_offset)
            if helpers.is_legal_pos(board, neighbour) and neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
