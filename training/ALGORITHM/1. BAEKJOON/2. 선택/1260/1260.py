N, M, V = map(int, input().split()) 
graph = [[0]*(N+1) for _ in range(N+1)] 
visited = [False]*(N+1)

for _ in range(M):
  x, y = map(int, input().split())
  graph[x][y] = 1 # 양방향 그래프 
  graph[y][x] = 1
 
def dfs(V): # 탐색 시작 정점 번호
  visited[V] = True # 방문한 인덱스는 True로 변경, 중복 해결
  print(V, end=" ")
  for i in range(1, N+1):
    if not visited[i] and graph[V][i] == 1: # 아직 방문하지 않은 곳 & 관계가 있는 곳
      dfs(i) # 재귀함수 시작, 다른 숫자로 이동

def bfs(V):
  visited[V] = False
  queue = [V]
  while queue:
    V = queue.pop(0)
    print(V, end=" ")
    for i in range(1, N+1):
      if visited[i] and graph[V][i] == 1:
        queue.append(i)
        visited[i] = False
dfs(V)
print()
bfs(V)