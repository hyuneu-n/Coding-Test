from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (N+1)
visited[1] = True

queue = deque([1])

while queue:
    curr = queue.popleft()

    for next in graph[curr]:
        if not visited[next]:
            visited[next] = True
            queue.append(next)

print(visited.count(True)-1)