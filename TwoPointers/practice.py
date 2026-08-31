from typing import List


class Solution:
    # 1. Valid Palindrome
    def isPalindrome(self, s: str) -> bool:
        pass

    # 2. Two Sum II - Input Array Is Sorted
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pass

    # 3. 3Sum
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass

    # 4. Container With Most Water
    def maxArea(self, heights: List[int]) -> int:
        pass

    # 5. Trapping Rain Water
    def trap(self, height: List[int]) -> int:
        pass


def normalize_triples(triples):
    """Order-insensitive form for 3Sum: sort within each triple and sort the list of
    triples, so a correct answer compares equal regardless of the order it was built in."""
    return sorted(sorted(t) for t in triples)


def run_tests():
    sl = Solution()
    tests = []

    def test_is_palindrome():
        assert sl.isPalindrome("A man, a plan, a canal: Panama") is True
        assert sl.isPalindrome("race a car") is False
    tests.append(("1. isPalindrome", test_is_palindrome))

    def test_two_sum():
        # Two Sum II returns 1-indexed positions.
        assert sl.twoSum([2, 7, 11, 15], 9) == [1, 2]
        assert sl.twoSum([2, 3, 4], 6) == [1, 3]
    tests.append(("2. twoSum", test_two_sum))

    def test_three_sum():
        result = sl.threeSum([-1, 0, 1, 2, -1, -4])
        expected = [[-1, -1, 2], [-1, 0, 1]]
        assert normalize_triples(result) == normalize_triples(expected)
    tests.append(("3. threeSum", test_three_sum))

    def test_max_area():
        assert sl.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    tests.append(("4. maxArea", test_max_area))

    def test_trap():
        assert sl.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    tests.append(("5. trap", test_trap))

    passed = 0
    for name, test_fn in tests:
        try:
            test_fn()
        except AssertionError:
            print(f"FAIL   {name}")
        except Exception as e:
            print(f"ERROR  {name}: {type(e).__name__}: {e}")
        else:
            print(f"PASS   {name}")
            passed += 1

    print(f"\n{passed}/{len(tests)} passed")


if __name__ == "__main__":
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(heights)

    sl = Solution()
    # Call whichever method you're practicing, e.g.:
    # print(sl.maxArea(heights))

    print()
    run_tests()
