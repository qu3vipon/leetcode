from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cache = defaultdict(int)
        for c in s:
            cache[c] += 1

        for c in t:
            if not cache[c]:
                return False
            else:
                cache[c] -= 1

        return sum(list(cache.values())) == 0