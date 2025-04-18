class Solution:
    def runLengthEncode(self, s: str) -> str:
        slow, fast = 0, 0
        n = len(s)
        res = ""
        while fast < n:
            count = 1
            while fast + 1 < n and s[fast] == s[fast + 1]:
                count += 1
                fast += 1
            res += s[slow] + str(count)
            slow = fast + 1
            fast = slow
        return res


    def runLengthDecode(self, s: str) -> str:
        n = len(s)
        res = ""
        slow, fast= 0, 1
        while fast < n:
            while fast < n and s[fast].isdigit():
                fast += 1
            res += s[slow] * int(s[slow + 1:fast])
            # Move slow to the next character after the digit
            slow = fast
            fast = slow + 1    

        return res

# Example usage:
if __name__ == "__main__":
    Solution = Solution()
    print(Solution.runLengthEncode("aaaaaaaaaabbbaxxxxyyyzyx"))  # Output: "a10b3a1x4y3z1y1x1"
    print(Solution.runLengthDecode("a10b3a1x4y3z1y1x1"))  # Output: "aaaaaaaaaabbbaxxxxyyyzyx"

    # Test cases
    assert Solution.runLengthEncode("aaaaaaaaaabbbaxxxxyyyzyx") == "a10b3a1x4y3z1y1x1"
    assert Solution.runLengthDecode("a10b3a1x4y3z1y1x1") == "aaaaaaaaaabbbaxxxxyyyzyx"
    assert Solution.runLengthEncode("a") == "a1"
    assert Solution.runLengthDecode("a1") == "a"
    assert Solution.runLengthEncode("abc") == "a1b1c1"
    assert Solution.runLengthDecode("a1b1c1") == "abc"

    print("All test cases passed!") 

