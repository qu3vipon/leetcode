class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for c in s:
            if c.isalnum():
                t += c.lower()
        return True

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            cl = s[l]
            cr = s[r]

            if not cl.isalnum():
                l += 1
                continue

            if not cr.isalnum():
                r -= 1
                continue

            if cl.lower() != cr.lower():
                return False

            l += 1
            r -= 1

        return True
