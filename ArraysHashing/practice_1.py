from typing import List
from collections import Counter, defaultdict


class Solution:
    # 1. Contains Duplicate
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)

        return False

    # 2. Valid Anagram
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)

        return s_counter == t_counter

    # 3. Two Sum
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return ([seen[diff], i])

            seen[num] = i

    # 4. Group Anagrams
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)

        for str in strs:
            char_count = [0] * 26
            for c in str:
                code = ord(c) - ord('a')
                char_count[code] += 1

            str_map[tuple(char_count)].append(str)

        return str_map.values()

    # 5. Top K Frequent Elements
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter for freq : list of nums
        freq_map = defaultdict(list)

        counter = Counter(nums)
        for num, freq in counter.items():
            freq_map[freq].append(num)

        res = []
        for i in range(len(nums), -1, -1):
            if i in freq_map:
                elements = freq_map[i]
                for element in elements:
                    res.append(element)
                    if len(res) == k:
                        return res



    # 6. Encode and Decode Strings
    def encode(self, strs: List[str]) -> str:
        encoded_str = []
        for s in strs:
            encoded_str.append(str(len(s)))
            encoded_str.append('#')
            encoded_str.append(s)

        return ''.join(encoded_str)

    def decode(self, s: str) -> List[str]:
        word_len = 0
        i = 0
        j = 0 
        res = []
        while i < len(s):
            if s[j] != '#':
                j += 1  
                continue

            word_len = int(s[i:j])
            j += 1
            res.append(s[j:j+word_len])
            i = j + word_len
            j = i 

        return res

    # 7. Product of Array Except Self
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        res = [0] * len(nums)

        prev_val = 1
        for i, num in enumerate(nums):
            prefix[i] = prev_val
            prev_val = prev_val * num

        prev_val = 1
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = prev_val
            prev_val = prev_val * nums[i]

        for i in range(len(nums)):
            res[i] = suffix[i] * prefix[i]
        return res
    


    # 8. Valid Sudoku
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        sub_box = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                val = board[row][col]
                if val == '.':
                    continue

                if val in row_set[row]:
                    return False
                row_set[row].add(val)

                if val in col_set[col]:
                    return False
                col_set[col].add(val)

                if val in sub_box[row//3, col//3]:
                    return False
                sub_box[row//3, col//3].add(val)

        return True

    # 9. Longest Consecutive Sequence
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_seq = 0
        for num in num_set:
            if num - 1 in num_set:
                continue

            curr_num = num
            curr_len = 1
            while curr_num+curr_len in num_set:
                curr_len += 1

            max_seq = max(max_seq, curr_len)
        return max_seq


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
