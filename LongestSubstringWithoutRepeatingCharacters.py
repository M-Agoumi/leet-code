class Solution:
    def lengthOfLongestSubstring(self, s):
        char_index = {}  # To store the index of each character
        start = 0  # Start index of the current substring
        max_length = 0  # Length of the longest substring without repeating characters

        for end in range(len(s)):
            if s[end] in char_index and char_index[s[end]] >= start:
                # If the current character is already in the substring, update the start index
                start = char_index[s[end]] + 1

            # Update the index of the current character
            char_index[s[end]] = end

            # Update the maximum length if the current substring is longer
            max_length = max(max_length, end - start + 1)

        return max_length


sol = Solution()
s = "abcabcbb"
print(sol.lengthOfLongestSubstring(s))