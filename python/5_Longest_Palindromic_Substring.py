class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Using the dynamic programming method, Not the fastest method
        # Time Complexity: O(N^2)
        length = len(s)
        if not length:
            return ''

        if length == 1:
            return s

        max_substring = ''
        substring = ''

        for i in range(length - 1):
            start = i
            end = i
            # First condition, "aba"
            while start >= 0 and end < length and s[start] == s[end]:
                start -= 1
                end += 1
            substring = s[start + 1:end]
            if len(substring) > len(max_substring):
                max_substring = substring

            # Second condition, "abba"
            start = i
            end = i + 1
            while start >= 0 and end < length and s[start] == s[end]:
                start -= 1
                end += 1
            substring = s[start + 1:end]

            if len(substring) > len(max_substring):
                max_substring = substring

        return max_substring
