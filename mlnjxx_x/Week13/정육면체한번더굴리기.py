from collections import deque

def getInput():
    # 입력받는 함수
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    return n, m, graph

def move(n, graph, dir, x, y, row, column):
    # 주사위를 굴리는 함수
    direction = [(0,1), (1,0), (0,-1), (-1,0)]  # 동남서북 (시계방향)
    nx, ny = x + direction[dir][0], y + direction[dir][1]
    if 0>nx or n==nx or 0>ny or n==ny:  # 벽에 부딪혔을 때
        dir = (dir+2)%4
        nx, ny = x + direction[dir][0], y + direction[dir][1]

    if dir==0:
        row.rotate(1)
        column[0] = row[0]
        column[2] = row[2]
    elif dir==1:
        column.rotate(-1)
        row[0] = column[0]
        row[2] = column[2]
    elif dir==2:
        row.rotate(-1)
        column[0] = row[0]
        column[2] = row[2]
    elif dir==3:
        column.rotate(1)
        row[0] = column[0]
        row[2] = column[2]

    if row[2]>graph[nx][ny]:
        dir = (dir+1)%4
    elif row[2]<graph[nx][ny]:
        dir = (dir+3)%4

    return dir, nx, ny, row, column

def score(n, graph, dir, x, y):
    direction = [(0,1), (1,0), (0,-1), (-1,0)]
    start = graph[x][y]
    q = deque([(x,y)])
    llist = {(x,y)}
    count = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + direction[i][0], y + direction[i][1]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==start and (nx,ny) not in llist:
                count+=1
                q.append((nx,ny))
                llist.add((nx,ny))

    return start*count


def main():
    n, m, graph = getInput()
    x, y = 0, 0
    dir = 0
    row = deque([1, 3, 6, 4])
    column = deque([1, 5, 6, 2])
    answer = 0

    for _ in range(m):
        dir, x, y, row, column = move(n, graph, dir, x, y, row, column)
        answer += score(n, graph, dir, x, y)

    print(answer)

main()