class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()        # empty set
        left = 0          # left pointer starts at 0
        max_length = 0    # start at 0
        
        for right in range(len(s)):
            while s[right] in window:    # while repeat exists
                window.remove(s[left])     # remove leftmost char
                left += 1               # move left forward
            window.add(s[right])          # add right char to window
            max_length = max(max_length, right - left + 1)  # window size
        
        return max_length