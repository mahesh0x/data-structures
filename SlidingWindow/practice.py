from typing import List


class Solution:
    # 1. Best Time to Buy and Sell Stock
    def maxProfit(self, prices: List[int]) -> int:
        pass

    # 2. Longest Substring Without Repeating Characters
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass

    # 3. Longest Repeating Character Replacement
    def characterReplacement(self, s: str, k: int) -> int:
        pass

    # 4. Permutation in String
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pass

    # 5. Minimum Window Substring
    def minWindow(self, s: str, t: str) -> str:
        pass

    # 6. Sliding Window Maximum
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pass


def run_tests():
    sl = Solution()
    tests = []

    def test_max_profit():
        assert sl.maxProfit([7, 1, 5, 3, 6, 4]) == 5
        assert sl.maxProfit([7, 6, 4, 3, 1]) == 0
    tests.append(("1. maxProfit", test_max_profit))

    def test_length_of_longest_substring():
        assert sl.lengthOfLongestSubstring("abcabcbb") == 3
        assert sl.lengthOfLongestSubstring("bbbbb") == 1
    tests.append(("2. lengthOfLongestSubstring", test_length_of_longest_substring))

    def test_character_replacement():
        assert sl.characterReplacement("AABABBA", 1) == 4
    tests.append(("3. characterReplacement", test_character_replacement))

    def test_check_inclusion():
        assert sl.checkInclusion("ab", "eidbaooo") is True
        assert sl.checkInclusion("ab", "eidboaoo") is False
    tests.append(("4. checkInclusion", test_check_inclusion))

    def test_min_window():
        assert sl.minWindow("ADOBECODEBANC", "ABC") == "BANC"
        assert sl.minWindow("a", "aa") == ""
    tests.append(("5. minWindow", test_min_window))

    def test_max_sliding_window():
        assert sl.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    tests.append(("6. maxSlidingWindow", test_max_sliding_window))

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
    prices = [7, 1, 5, 3, 6, 4]
    print(prices)

    sl = Solution()
    # Call whichever method you're practicing, e.g.:
    # print(sl.maxProfit(prices))

    print()
    run_tests()
