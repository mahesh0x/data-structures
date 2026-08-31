from typing import List


class Solution:
    # 1. Subsets
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            
            res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])
        return res

    # 2. Combination Sum
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start, target, path):

            if target == 0:
                res.append(path[:])

            for i in range(start, len(candidates)):

                if i > 0 and candidates[i] == candidates[i-1]:
                    continue

                if target - candidates[i] < 0:
                    break

                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return res


    # 3. Permutations
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()

        def backtrack(path, visited):

            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(0, len(nums)):
                if i in visited:
                    continue

                visited.add(i)
                path.append(nums[i])

                backtrack(path, visited)

                visited.remove(i)
                path.pop()
            
        backtrack([], visited)
        return res


    # 4. Subsets II
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(start, path):
            res.append(path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue

                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])
        return res

    # 5. Combination Sum II
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start, target, path):
            # answer
            if target == 0:
                res.append(path[:])

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                if candidates[i] > target:
                    break

                path.append(candidates[i])
                backtrack(i+1, target-candidates[i], path)
                path.pop()
        
        backtrack(0, target, [])
        return res


    # 6. Word Search
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass

    # 7. Palindrome Partitioning
    def partition(self, s: str) -> List[List[str]]:
        pass

    # 8. Letter Combinations of a Phone Number
    def letterCombinations(self, digits: str) -> List[str]:
        pass

    # 9. N-Queens
    def solveNQueens(self, n: int) -> List[List[str]]:
        pass


def norm(solutions, sort_inner=False):
    """Order-insensitive comparison for backtracking results, which may come out in any order.
    Sorts the outer list of solutions; set sort_inner=True when the elements *within* a single
    solution are also order-free (subsets, combinations) rather than meaningful (permutations,
    partitions, board rows)."""
    prepared = [sorted(s) if sort_inner else list(s) for s in solutions]
    return sorted(prepared)


def run_tests():
    sl = Solution()
    tests = []

    def test_subsets():
        expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
        assert norm(sl.subsets([1, 2, 3]), True) == norm(expected, True)
    tests.append(("1. subsets", test_subsets))

    def test_combination_sum():
        expected = [[2, 2, 3], [7]]
        assert norm(sl.combinationSum([2, 3, 6, 7], 7), True) == norm(expected, True)
    tests.append(("2. combinationSum", test_combination_sum))

    def test_permute():
        expected = [
            [1, 2, 3], [1, 3, 2], [2, 1, 3],
            [2, 3, 1], [3, 1, 2], [3, 2, 1],
        ]
        assert norm(sl.permute([1, 2, 3])) == norm(expected)
    tests.append(("3. permute", test_permute))

    def test_subsets_with_dup():
        expected = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
        assert norm(sl.subsetsWithDup([1, 2, 2]), True) == norm(expected, True)
    tests.append(("4. subsetsWithDup", test_subsets_with_dup))

    def test_combination_sum2():
        expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        result = sl.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
        assert norm(result, True) == norm(expected, True)
    tests.append(("5. combinationSum2", test_combination_sum2))

    def test_exist():
        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ]
        assert sl.exist(board, "ABCCED") is True
        assert sl.exist(board, "ABCB") is False
    tests.append(("6. exist", test_exist))

    def test_partition():
        expected = [["a", "a", "b"], ["aa", "b"]]
        assert norm(sl.partition("aab")) == norm(expected)
    tests.append(("7. partition", test_partition))

    def test_letter_combinations():
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        assert sorted(sl.letterCombinations("23")) == sorted(expected)
    tests.append(("8. letterCombinations", test_letter_combinations))

    def test_solve_n_queens():
        expected = [
            [".Q..", "...Q", "Q...", "..Q."],
            ["..Q.", "Q...", "...Q", ".Q.."],
        ]
        result = sl.solveNQueens(4)
        assert norm(result) == norm(expected)
    tests.append(("9. solveNQueens", test_solve_n_queens))

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
    nums = [1, 2, 3]
    print(nums)

    sl = Solution()
    # Call whichever method you're practicing, e.g.:
    # print(sl.subsets(nums))

    print()
    run_tests()
