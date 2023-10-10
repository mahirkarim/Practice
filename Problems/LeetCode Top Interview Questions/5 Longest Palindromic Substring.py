class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # correct but time too slow, consider dynamic
        if s == '':
            return ''
        longest = 1
        substring = s[0]

        for x in range(len(s)):
            for y in range(x+1, len(s)):
                curr_len = 1
                if s[x] == s[y]:
                    for i in range(y-x):
                        if s[x+i] == s[y-i]:
                            curr_len += 1
                        else:
                            curr_len = 1
                            break
                    if curr_len > longest:
                        longest = curr_len
                        substring = s[x:y+1]
        return substring
        

        