class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num_set1 = list(set(nums1))
        num_set2 = list(set(nums2))
        answer = []
        for num in num_set1:
            if num in num_set2:
                answer.append(num)

        return answer