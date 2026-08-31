from typing import List


class Solution:
    # 1. Contains Duplicate
    def containsDuplicate(self, nums: List[int]) -> bool:
        pass

    # 2. Valid Anagram
    def isAnagram(self, s: str, t: str) -> bool:
        pass

    # 3. Two Sum
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pass

    # 4. Group Anagrams
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pass

    # 5. Top K Frequent Elements
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pass

    # 6. Encode and Decode Strings
    def encode(self, strs: List[str]) -> str:
        pass

    def decode(self, s: str) -> List[str]:
        pass

    # 7. Product of Array Except Self
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pass

    # 8. Valid Sudoku
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        pass

    # 9. Longest Consecutive Sequence
    def longestConsecutive(self, nums: List[int]) -> int:
        pass


def normalize_groups(groups):
    """Order-insensitive form for Group Anagrams: sort within each group and sort the
    groups, so a correct answer compares equal regardless of the order it was built in."""
    return sorted(sorted(g) for g in groups)


def run_tests():
    sl = Solution()
    tests = []

    def test_contains_duplicate():
        assert sl.containsDuplicate([1, 2, 3, 1]) is True
        assert sl.containsDuplicate([1, 2, 3, 4]) is False
    tests.append(("1. containsDuplicate", test_contains_duplicate))

    def test_is_anagram():
        assert sl.isAnagram("anagram", "nagaram") is True
        assert sl.isAnagram("rat", "car") is False
    tests.append(("2. isAnagram", test_is_anagram))

    def test_two_sum():
        assert sl.twoSum([2, 7, 11, 15], 9) == [0, 1]
        assert sl.twoSum([3, 2, 4], 6) == [1, 2]
    tests.append(("3. twoSum", test_two_sum))

    def test_group_anagrams():
        result = sl.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        assert normalize_groups(result) == normalize_groups(expected)
    tests.append(("4. groupAnagrams", test_group_anagrams))

    def test_top_k_frequent():
        assert sorted(sl.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    tests.append(("5. topKFrequent", test_top_k_frequent))

    def test_encode_decode():
        strs = ["neet", "code", "love", "you"]
        assert sl.decode(sl.encode(strs)) == strs
        # A payload that contains delimiter-like characters must still round-trip.
        tricky = ["4#word", "", "a#b"]
        assert sl.decode(sl.encode(tricky)) == tricky
    tests.append(("6. encode/decode", test_encode_decode))

    def test_product_except_self():
        assert sl.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    tests.append(("7. productExceptSelf", test_product_except_self))

    def test_valid_sudoku():
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        assert sl.isValidSudoku(board) is True
    tests.append(("8. isValidSudoku", test_valid_sudoku))

    def test_longest_consecutive():
        assert sl.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    tests.append(("9. longestConsecutive", test_longest_consecutive))

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
    nums = [1, 2, 3, 1]
    print(nums)

    sl = Solution()
    # Call whichever method you're practicing, e.g.:
    # print(sl.containsDuplicate(nums))

    print()
    run_tests()
