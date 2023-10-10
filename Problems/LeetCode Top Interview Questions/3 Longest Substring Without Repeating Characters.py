class Solution(object):
    # solution faster than 48%, less memory than 49%
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        long_x = 0
        long_y = 1

        curr_x = 0

        long_len = 1
        copy_s = s
        curr_sub = s[long_x:long_y]
        for i in range(1, len(s)):
            
            if str(s[i]) not in str(curr_sub):
                curr_sub = s[curr_x:i+1]
                continue

            curr_len = i - curr_x

            if curr_len > long_len:
                long_len = curr_len
                long_x = curr_x
                long_y = i
            
            idx = curr_sub
            curr_x = curr_x + curr_sub.index(s[i]) + 1
            curr_sub = s[curr_x:i+1]
        if len(curr_sub) > len(s[long_x:long_y]):
            return len(curr_sub)
        return len(s[long_x:long_y])