class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for n in nums:
            if (n-1) not in s:
                m = n + 1
                while m in s:
                    m += 1
                ans = max(ans, m-n)
        return ans