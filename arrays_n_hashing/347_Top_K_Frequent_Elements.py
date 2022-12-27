from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        ans = []
        for i, (n, c) in enumerate(sorted(counter.items(), key=lambda x: x[1], reverse=True), 1):
            ans.append(n)
            if i == k:
                return ans