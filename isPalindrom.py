class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        rev = 0
        while x > 0:
            dig = (x % 10)
            rev = (rev * 10) + dig
            x = x // 10
        if (temp == rev):
            return True
        else:
            return False
s = Solution()
print(s.isPalindrome(121))
