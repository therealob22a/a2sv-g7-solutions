def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    idx1=0
    idx2=0

    sol = []

    while idx1<n and idx2<m:
        if a[idx1]<b[idx2]:
            sol.append(a[idx1])
            idx1+=1
        else:
            sol.append(b[idx2])
            idx2+=1
    
    while idx1<n:
        sol.append(a[idx1])
        idx1+=1

    while idx2<m:
        sol.append(b[idx2])
        idx2+=1
    
    print(*sol)

solve()
