from typing import List


class Solution:
    # 1. Valid Palindrome
    def isPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s) - 1

        while i <= j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True

    # 2. Two Sum II - Input Array Is Sorted
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            curr_sum = numbers[l] + numbers[r]

            if curr_sum < target:
                l += 1
            elif curr_sum > target:
                r -= 1
            else:
                return [l+1, r+1]


        

    # 3. 3Sum
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum == 0:
                    res.append([nums[i], nums[l], nums[r]])

                if curr_sum > 0:
                    r -= 1
                else:
                    l += 1

        return res


    # 4. Container With Most Water
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1

        max_area = 0 
        while l < r:
            min_height = min(heights[r], heights[l])
            area = (r-l) * min_height
            max_area = max(max_area, area)

            if l < r:
                l += 1
            else:
                r -= 1

        return max_area

    # 5. Trapping Rain Water
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        l_max, r_max = height[l], height[r]
        res = 0

        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(height[l], l_max)
                res += l_max - height[l]
            else:
                r -= 1
                r_max = max(height[r], r_max)
                res += r_max - height[r]

        return res

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
