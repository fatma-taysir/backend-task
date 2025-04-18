class Solution:
    def palindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            # check if characters are non-alphanumeric
            # and move the pointers accordingly
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            # Check if characters are equal
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True 
    

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    test_cases = ["level", "anna", "noon", "rotator", "a", "   ", "  A  ", "Apple", "No 'x' in Nixon"]

    for test in test_cases:
        result = solution.palindrome(test)
        print(f"Input: '{test}' => Output: {result}")

    # Test cases
    assert solution.palindrome("level") is True
    assert solution.palindrome("anna") is True
    assert solution.palindrome("noon") is True
    assert solution.palindrome("rotator") is True
    assert solution.palindrome("a") is True
    assert solution.palindrome("   ") is True
    assert solution.palindrome("  A  ") is True
    assert solution.palindrome("Apple") is False
    assert solution.palindrome("No 'x' in Nixon") is True
    

    print("All test cases passed!")
