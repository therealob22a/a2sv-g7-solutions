grid = [list(map(int,input().split())) for _ in range(5)]
for i in range(5):
    for j in range(5):
        if grid[i][j] == 1:
            break
    if grid[i][j] == 1:
        break
print(abs(2-i)+abs(2-j))