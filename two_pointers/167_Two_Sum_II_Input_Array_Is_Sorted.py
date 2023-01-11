class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s, e = 0, len(numbers) - 1

        while s < e:
            n = numbers[s] + numbers[e]

            if n == target:
                return [s + 1, e + 1]
            elif n < target:
                s += 1
            elif n > target:
                e -= 1