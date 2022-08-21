n = map(int, input().split())  # 좌표의 크기를 받아준다
plans = input().split() # 이동경로를 입력한다 
x, y = 1, 1 #최초의 좌표위치 값 설정

move_types = ['L', 'R', 'U', 'D'] # 움직일 수 있는 경로 방향키 설정
dx = [0, 0, -1, 1] # 오른쪽으로 이동시 1,1 -> 1, 2 -> 1,3 으로 y변경 / 아래쪽으로 이동시 1,1 -> 2,1 -> 3,1 으로 x변경
dy = [-1, 1, 0, 0]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]: # 내 입력 플랜과 움직이는 방향키가 똑같을 경우에 dx에 있는 이동경로만큼 움직일 수 있도록 각각 x, y에 더해준다.
            nx = x + dx[i]
            ny = y + dy[i]
            
    if nx < 1 or ny < 1 or nx > n or ny > n: # n * n의 경로를 벗어나도 상관하지 않도록 설정
        continue
    
    x, y = nx, ny
    
print(x, y )

            