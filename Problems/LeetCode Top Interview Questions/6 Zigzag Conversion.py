class Solution(object):
    # slow and memory intensive, but passes
    # def convert(self, s, numRows):
    #     """
    #     :type s: str
    #     :type numRows: int
    #     :rtype: str
    #     """

    #     if numRows > len(s):
    #         return s
    #     if numRows == 1:
    #         return s
    #     x = 0
    #     y = 0
    #     ascending = 0
    #     matrix_dict = dict()
    #     for c in s:
    #         if ascending:
    #             x += 1
    #             y -= 1
    #             for i in range(numRows):
    #                 matrix_dict[x,i] = ''
    #             matrix_dict[x, y] = c
    #         else:
    #             matrix_dict[x, y] = c
    #             y += 1
    #         if y == 0:
    #             ascending = 0
    #             y += 1
    #         elif y == numRows:
    #             ascending = 1
    #             y -= 1
        
    #     return_string = ''

    #     for i in range(numRows):
    #         for j in range(0, x+1):
    #             return_string += matrix_dict[j, i]
    #     return return_string

    # much better, but still pretty slow
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

        rows_dict = dict()
        for row in range(numRows):
            rows_dict[row] = []

        row = 0
        ascending = 0

        for c in s:
            if ascending:
                row -= 1 
                rows_dict[row].append(c)
            else:
                rows_dict[row].append(c)
                row += 1
            if row == 0:
                ascending = 0
                row += 1
            elif row == numRows:
                ascending = 1
                row -= 1
        
        return_string = ''

        for row in range(numRows):
            return_string += ''.join(rows_dict[row])
        return return_string