# DFS 음료수 채우기 
# n, m 을 공백으로 구분하여 입력받기 
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보를 입력받기
graph = []
for i in range(n):
    graph.append(map(int, input().split()))

# dfs로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문    
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드들을 방문하지 않았다면
    if graph[x][y] == 0:
        #해당 노드를 방문처리
        graph[x][y] = 1
        #상하좌우 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# 모든 노드에 대해 음료수 채우기 
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == 0:
            result += 1
            
print(result)
        