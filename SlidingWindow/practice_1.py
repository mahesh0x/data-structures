from typing import List
from collections import defaultdict, Counter


class Solution:
    # 1. Best Time to Buy and Sell Stock
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, len(prices)-1
        max_profit = 0

        for r in range(len(prices)):
            if prices[l] < prices[r]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r
            r += 1

        return max_profit

    # 2. Longest Substring Without Repeating Characters
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        char_set = set()
        l, r = 0, 0
        max_len = 0

        for r in range(len(s)):
            incoming_char = s[r]

            while incoming_char in char_set:
                char_set.remove(s[l])
                l += 1

            char_set.add(incoming_char)
            max_len = max(max_len, (r-l+1))

        return max_len
    
    # 3. Longest Repeating Character Replacement
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = defaultdict(int)
        l = 0
        max_freq = 0
        max_len = 0

        for r in range(len(s)-1):
            incoming_char = s[r]

            char_freq[incoming_char] += 1
            max_freq = max(max_freq, char_freq[incoming_char])

            if (r-l+1) - max_freq > k:
                char_freq[s[l]] -= 1
                l += 1

            max_len = max(max_len, (r-l+1))

        return max_len

    # 4. Permutation in String
    def checkInclusion(self, s1: str, s2: str) -> bool:
        print(s1, s2)
        if len(s2) < len(s1):
            return False

        s1_counter = Counter(s1)
        s2_counter = defaultdict(int)
        for c in s2[:len(s1)]:
            s2_counter[c] += 1

        l = 0 
        r = len(s1)

        if s1_counter == s2_counter:
            return True

        while r < len(s2):
            outgoing_char = s2[l]
            incoming_char = s2[r]

            s2_counter[outgoing_char] -= 1
            if s2_counter[outgoing_char] == 0:
                del s2_counter[outgoing_char]

            s2_counter[incoming_char] += 1

            if s1_counter == s2_counter:
                return True
            r += 1
            l += 1

        return False
        

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
        assert sl.maxProfit([2,1,4]) == 3
        assert sl.maxProfit([2,1,2,1,0,1,2]) == 2
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
