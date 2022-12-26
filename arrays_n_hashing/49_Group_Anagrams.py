from collections import Counter
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = defaultdict(list)
        for s in strs:
            c = Counter(s)
            k = ""
            for a, b in sorted(list(c.items()), key=lambda x: x[0]):
                k += a + str(b)
            g[k].append(s)
        return [v for v in g.values()]

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            g[tuple(count)].append(s)
        return [v for v in g.values()]
