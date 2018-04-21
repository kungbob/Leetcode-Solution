class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Iterate the string
        substring = dict()
        longest = 0
        substring_length = 0
        i = 0
        # Start point of the substring
        start = 0
        for char in s:
            if char in substring:
                last_appearance = substring[char]
                
                # Reset the substring start point
                if last_appearance > start:
                    start = last_appearance
                substring_length = i - start
                substring[char] = i

            else :
                substring[char] = i
                substring_length += 1

            if substring_length > longest:
                longest = substring_length
            i += 1

        return longest
