class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        a = [1] * l
        b = [1] * l

        tmp = 1
        for i, n in enumerate(nums):
            tmp *= n
            a[i] = tmp

        tmp = 1
        for i, n in enumerate(nums[::-1]):
            tmp *= n
            b[l - i - 1] = tmp

        a.append(1)
        b.append(1)

        return [a[i - 1] * b[i + 1] for i in range(l)]