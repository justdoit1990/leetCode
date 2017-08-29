class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diff = {}
        for i in range(len(nums)):
            if diff.has_key(nums[i]):
                return [nums.index(diff[nums[i]]), i]
            else:
                diff[target-nums[i]] = nums[i]

