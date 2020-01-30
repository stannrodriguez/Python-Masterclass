class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        if len(set(s)) == 1:
            return s
        if len(s) > 1000:
            return

        def isPalindrome(x):
            return x[::-1] == x

        longestP = ''
        n = len(s)
        for i, char in enumerate(s):
            current_str = char
            for inc in range(1, i+1):
                current_str = s[i-inc:i+inc]
                if isPalindrome(current_str):   
                    if len(current_str) > len(longestP):
                        longestP = current_str
                else:
                    break

            for inc in range(1, i+1):
                current_str = s[i-inc:i+inc+1]
                if isPalindrome(current_str):
                    if len(current_str) > len(longestP):
                        longestP = current_str
                    current_str = s[i-inc+1:i+inc+2]
                    inc += 1
                else:
                    break
        if len(longestP) == 0:
            return s[0]

        return longestP


print(Solution().longestPalindrome('babad'))
print(Solution().longestPalindrome('cbbd'))
print(Solution().longestPalindrome('123454321'))
print(Solution().longestPalindrome('bb'))
print(Solution().longestPalindrome('ba'))
print(Solution().longestPalindrome('abcdef'))