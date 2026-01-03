class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = -1
        left_sum = -1
        right_sum = 0
        for i in range(len(nums)):
            left_sum = sum(nums[:i])
            print(left_sum)
            right_sum = sum(nums[i+1:])
            if left_sum == right_sum:
                return i
        return pivot