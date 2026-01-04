class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        answer_0,answer_1 = [],[]
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                answer_0.append(nums1[i])
        for j in range(len(nums2)):
            if nums2[j] not in nums1:
                answer_1.append(nums2[j])
        answer_0, answer_1 = set(answer_0),set(answer_1)
        answer_0, answer_1 = list(answer_0), list(answer_1)
        answer.append(answer_0)
        answer.append(answer_1)
        return answer