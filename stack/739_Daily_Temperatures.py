class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i, v in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < v:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans
