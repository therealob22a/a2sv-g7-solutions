def solve():
    n,m=map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))


    sol=[]
    first = 0

    for second in range(m):
        while first<n and a[first]<b[second]:
            first+=1
        sol.append(first)

    print(*sol)

solve()
