from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    row_l, row_r = 0, len(matrix) - 1
    c_l, c_r = 0, len(matrix[0]) - 1
    while row_l <= row_r:
        m = (row_r + row_l) // 2
        if matrix[m][c_l] <= target <= matrix[m][c_r]:
            while c_l <= c_r:
                m_c = (c_r + c_l) // 2
                if matrix[m][m_c] == target:
                    return True
                elif matrix[m][m_c] > target:
                    c_r = m_c - 1
                else:
                    c_l = m_c + 1
            else:
                return False

        elif matrix[m][c_l] > target:
            row_r = m - 1
        else:
            row_l = m + 1
    return False


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    assert True is searchMatrix(matrix, target), 'test 1'

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    assert False is searchMatrix(matrix, target), 'test 2'
