class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        prod = 1
        for num in nums:
            prod = prod*num
        
        if prod>0:
            return 1
        elif prod<0:
            return -1
        else:
            return 0
        
