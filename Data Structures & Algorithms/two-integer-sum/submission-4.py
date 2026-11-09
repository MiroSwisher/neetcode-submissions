class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNums = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in seenNums:
                return [seenNums[complement], i]
            else:
                seenNums[n] = i