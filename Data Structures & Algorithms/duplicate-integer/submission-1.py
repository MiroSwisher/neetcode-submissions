class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_ver = set(nums)
        return len(nums) != len(set_ver)
        