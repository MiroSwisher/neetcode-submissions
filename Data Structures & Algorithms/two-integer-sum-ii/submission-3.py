class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapped_nums = {}
        for i, n in enumerate(numbers):
            mapped_nums[n] = i
        
        for i in range(len(numbers)):
            need = target - numbers[i]
            if need in mapped_nums:
                return [i + 1, mapped_nums[need] + 1]
