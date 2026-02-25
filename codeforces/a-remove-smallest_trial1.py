def countingSort(arr):
    histogram = [0]*max(arr)
    for num in arr:
        histogram[num-1]+=1
    
    index = 0
    for idx,val in enumerate(histogram):
        for _ in range(val):
            arr[index]=idx+1
            index+=1

def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    countingSort(arr)

    for i in range(n-1):
        if arr[i+1]-arr[i]>1:
            print("NO")
            return
    print("YES")

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        solve()