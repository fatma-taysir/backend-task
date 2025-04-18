# Problem 5: Unique Elements
from typing import List
class Solution:
    def unique(self, arr) :
        unique:  List[str] = []
        for s in arr:
            if s not in unique:
                # If the string is not in unique, add it
                unique.append(s)
            else:
                unique.remove(s)
       
        return unique



# Example usage:
if __name__== "__main__" :
    Solution = Solution()
    Solution.unique(['apples', 'oranges', 'flowers', 'apples']) # returns ['oranges', 'flowers'] 
    Solution.unique(['apples', 'apples']) # returns [] 
    Solution.unique(['apples']) # returns ['apples']

    print(Solution.unique(['apples', 'oranges', 'flowers', 'apples']))  # Output: ['oranges', 'flowers']
    print(Solution.unique(['apples', 'apples']))  # Output: []
    print(Solution.unique(['apples']))  # Output: ['apples']

    # Test cases
    assert Solution.unique(['apples', 'oranges', 'flowers', 'apples']) == ['oranges', 'flowers']
    assert Solution.unique(['apples', 'apples']) == []
    assert Solution.unique(['apples']) == ['apples']

    print("All test cases passed!")
