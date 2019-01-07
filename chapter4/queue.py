from collections import deque
from typing import Deque


class Task:
    def __init__(self, taskname: str, tasktime: int) -> None:
        self.name = taskname
        self.time = tasktime


n, q = map(int, input().split())
queue: Deque[Task] = deque()
for i in range(n):
    name, time = input().split()
    task = Task(name, int(time))
    queue.append(task)

elaps = 0
while len(queue) > 0:
    task = queue.popleft()
    c = min(q, task.time)
    task.time -= c
    elaps += c
    if task.time > 0:
        queue.append(task)
    else:
        print("{0} {1}".format(task.name, elaps))
