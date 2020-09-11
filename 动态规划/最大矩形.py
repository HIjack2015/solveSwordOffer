def print_matrix( matrix:[[]]):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            ele = int(matrix[row][column])
            print(str(ele),end=" ")
        print("")


class Solution:
    def maximalRectangle(self, matrix: [[str]]) -> int:

        if not matrix or not matrix[0]:
            return 0

        row_count=len(matrix)
        column_count=len(matrix[0])
        max_area = 0
        left=[0]*column_count
        right=[column_count]*column_count
        height=[[0]*column_count for i in range(row_count)]

        for row in range(row_count):
            cur_left,cur_right=0,column_count

            for column in range(column_count):
                ele=int(matrix[row][column])

                if row==0 or ele==0:
                    height[row][column]=ele
                else:
                    height[row][column]=height[row-1][column]+1

                if ele:
                    left[column]=max(cur_left,left[column])
                else:
                    left[column]=0
                    cur_left=column+1

            for column in range(column_count-1,-1,-1):
                ele = int(matrix[row][column])

                if ele:
                    right[column]=min(right[column],cur_right)
                else:
                    right[column]=column_count
                    cur_right=column
            for column in range(len(matrix[0])):
                left_value = left[column]
                right_value  =right[column]
                height_value = height[row][column]
                this_area=(right_value-left_value)*height_value
                max_area=max(this_area,max_area)

        return max_area

a=[[]]


res=Solution().maximalRectangle(a)
print(str(res))