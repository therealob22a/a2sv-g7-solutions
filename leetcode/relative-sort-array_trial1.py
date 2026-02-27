class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        size = max(arr1)+1
        count = [0]*size
        for num in arr1:
            count[num]+=1
        
        sol = []
        for num in arr2:
            for _ in range(count[num]):
                sol.append(num)
            count[num]=0
        
        for idx in range(size):
            for _ in range(count[idx]):
                sol.append(idx)

        return sol
