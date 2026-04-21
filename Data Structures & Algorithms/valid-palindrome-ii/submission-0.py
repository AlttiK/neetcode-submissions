class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum()).lower()
        print(s)

        left = 0
        right = len(s) - 1

        hasChangedOne = False

        while left <= right:
            if s[left] != s[right]:
                skipLeft, skipRight = s[left + 1:right+1], s[left:right]
                return skipLeft[::-1] == skipLeft or skipRight[::-1] == skipRight
            left += 1
            right -= 1
        
        return True