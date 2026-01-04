class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[],[]]
        answer_0,answer_1 = set(nums1),set(nums2)
        for i in answer_0:
            if i not in nums2:
                answer[0].append(i)
        for j in answer_1:
            if j not in nums1:
                answer[1].append(j)
        
        return answer