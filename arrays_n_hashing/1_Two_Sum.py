class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i+1:], i+1):
                if a + b == target:
                    return [i, j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = dict()
        for i, n in enumerate(nums):
            d = target - n
            if d in c:
                return [c[d], i]
            c[n] = i
