# Problem 6: Transpose
class Solution:
    def transpose(self, matrix) :
        # Transpose the matrix
        transposed = []
        for col in range(len(matrix[0])):
            new_row = []
            for row in range(len(matrix)):
                new_row.append(matrix[row][col])
            transposed.append(new_row)
        return transposed


# Example usage:

if __name__== "__main__" :
    Solution = Solution()
    print(Solution.transpose( [ [1,2], [3,4] ] )) # returns [ [1,3], [2,4] ]
    print(Solution.transpose( [ [1,2,3,4], [5,6,7,8] ] ))  # returns [ [1,5], [2,6], [3,7], [4,8] ])

    # Test cases
    assert Solution.transpose( [ [1,2], [3,4] ] ) == [ [1,3], [2,4] ]
    assert Solution.transpose( [ [1,2,3,4], [5,6,7,8] ] ) == [ [1,5], [2,6], [3,7], [4,8] ]

    print("All test cases passed!")