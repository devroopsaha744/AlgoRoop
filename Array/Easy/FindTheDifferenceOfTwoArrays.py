class Solution(object):
    def findDifference(self, nums1, nums2):
        nums1  = list(set(nums1))
        nums2 = list(set(nums2))

        arr1 = []
        arr2 = []
        for num in nums1:
            if(num not in nums2):
                arr1.append(num)
        
        for num in nums2:
            if(num not in nums1):
                arr2.append(num)
        
        answer = [arr1, arr2]

        return answer