class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = [1] * len(nums) # first index has nothing to the left of it
        suffix_arr = [1] * len(nums) # last index has nothing to the right of it
        result = [0] * len(nums)
        for i in range(1, len(nums)):
            prefix_arr[i] = nums[i - 1] * prefix_arr[i - 1]
            
        for i in range(len(nums) - 2, -1, -1):
            suffix_arr[i] = nums[i + 1] * suffix_arr[i + 1]

        for i in range(len(nums)):
            result[i] = prefix_arr[i] * suffix_arr[i]
        return result
        

