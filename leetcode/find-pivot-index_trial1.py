class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left_sum = 0
        total_sum = sum(nums)

        for idx in range(n):
            if total_sum-nums[idx] == 2*left_sum:
                return idx
            left_sum+=nums[idx]
        
        return -1