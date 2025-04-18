# Problem 8: Index of First Duplication

class Solution:
    def index_of_first_duplicate(self, arr):
        seen =  set()

        for i in range(len(arr)):
            # Check if the current element is already in the seen list
            if arr[i] not in seen:
                # If not, add it to the seen list
                seen.add(arr[i])
            else:
                # If it is, return the index of the first duplicate
                return i 
        # If no duplicates are found, return -1                 
        return -1

#  Time Complexity: O(n), where n is the length of the input array.
#  Space Complexity: O(n), where n is the length of the input array.    


# Example usage:
if __name__== "__main__" :
    Solution = Solution()
    print(Solution.index_of_first_duplicate([ 5, 17, 3, 17, 4, -1 ]))  # Output: 3

    # Test cases
    assert Solution.index_of_first_duplicate([5, 17, 3, 17, 4, -1]) == 3
    assert Solution.index_of_first_duplicate([1, 2, 3, 4, 5]) == -1
    assert Solution.index_of_first_duplicate([1, 2, 3, 1]) == 3

print("All test cases passed!")