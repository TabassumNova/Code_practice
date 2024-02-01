class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        resLen = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                l -= 1
                r += 1
        if resLen == len(s):
            return True
        else:
            return False

    def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False
        reversed = 0
        temp = x
        while temp != 0:
            digit = temp % 10
            reversed = reversed * 10 + digit
            temp = temp // 10
        if reversed == x:
            return True
        else:
            return False

    def isPalindrome3(self, x: str) -> bool:

        i = 0
        j = len(x) - 1
        while i<=j:
            if x[i] == x[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

if __name__ == "__main__":
    text = '1221'
    s = Solution()
    result = s.isPalindrome3(text)
    pass