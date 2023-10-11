class Solution(object):
    # slow and memory intensive, but passes
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows > len(s):
            return s
        if numRows == 1:
            return s
        x = 0
        y = 0
        ascending = 0
        matrix_dict = dict()
        for c in s:
            if ascending:
                x += 1
                y -= 1
                for i in range(numRows):
                    matrix_dict[x,i] = ''
                matrix_dict[x, y] = c
            else:
                matrix_dict[x, y] = c
                y += 1
            if y == 0:
                ascending = 0
                y += 1
            elif y == numRows:
                ascending = 1
                y -= 1
        
        return_string = ''

        for i in range(numRows):
            for j in range(0, x+1):
                return_string += matrix_dict[j, i]
        return return_string