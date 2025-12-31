class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n < k:
            return -1
        if n == 1:
            return nums[0]
        window_sum = sum(nums[:k])
        max_avg = window_sum/k
        for i in range(k,n):
            window_sum = window_sum - nums[i-k] + nums[i]
            curr_avg = (window_sum)/k
            if curr_avg > max_avg:
                max_avg = curr_avg
        return max_avg