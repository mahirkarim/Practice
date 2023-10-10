class Solution(object):
    # solution faster than 48%, less memory than 49%
    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
        
    #     long_x = 0
    #     long_y = 1

    #     curr_x = 0

    #     long_len = 1
    #     curr_sub = s[long_x:long_y]
    #     for i in range(1, len(s)):
            
    #         if s[i] not in str(curr_sub):
    #             curr_sub = s[curr_x:i+1]
    #             continue

    #         curr_len = i - curr_x

    #         if curr_len > long_len:
    #             long_len = curr_len
    #             long_x = curr_x
    #             long_y = i
            
            
    #         curr_x = curr_x + curr_sub.index(s[i]) + 1
    #         curr_sub = s[curr_x:i+1]
    #     if len(curr_sub) > len(s[long_x:long_y]):
    #         return len(curr_sub)
    #     return len(s[long_x:long_y])
    

    # this solution beats 90% in speed 22% in memory
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        curr_x = 0

        long_len = 0
        curr_sub = ''
        curr_len = 0

        for i in range(0, len(s)):
            
            if s[i] not in curr_sub:
                curr_sub = s[curr_x:i+1]
                curr_len = i - curr_x + 1
                continue

            curr_len = i - curr_x

            curr_x = curr_x + curr_sub.index(s[i]) + 1
            curr_sub = s[curr_x:i+1]

            if curr_len > long_len:
                long_len = curr_len
        
        if curr_len > long_len:
            return curr_len
        print(curr_sub)
        return long_len