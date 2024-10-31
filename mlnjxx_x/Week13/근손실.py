import sys
input = sys.stdin.readline
N,K = map(int,input().split())
kit = list(map(int,input().split()))
visited = [False] * N
answer = 0
def dfs(depth,weight):
    global answer
    if depth == N:
        answer += 1
        return
    if weight < 500:
        return
    for i in range(N):
        if visited[i]:
            continue
        else:
            visited[i] = True
            dfs(depth+1,weight + kit[i] - K)
            visited[i] = False
dfs(0,500)
print(answer)

