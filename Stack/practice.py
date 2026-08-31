from typing import List


# 2. Min Stack
# A design problem: implement the class so every operation is O(1). Track the running
# minimum alongside each pushed value so getMin() never has to scan the stack.
class MinStack:
    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
        pass


class Solution:
    # 1. Valid Parentheses
    def isValid(self, s: str) -> bool:
        paranthesis_map = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []

        for c in s:
            if c not in paranthesis_map:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                
                last_element = stack.pop()
                if last_element != paranthesis_map[c]:
                    return False

        return len(stack) == 0

    # 3. Evaluate Reverse Polish Notation
    def evalRPN(self, tokens: List[str]) -> int:
        pass

    # 4. Generate Parentheses
    def generateParenthesis(self, n: int) -> List[str]:
        pass

    # 5. Daily Temperatures
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pass

    # 6. Car Fleet
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pass

    # 7. Largest Rectangle in Histogram
    def largestRectangleArea(self, heights: List[int]) -> int:
        pass


def run_tests():
    sl = Solution()
    tests = []

    def test_is_valid():
        assert sl.isValid("()[]{}") is True
        assert sl.isValid("(]") is False
    tests.append(("1. isValid", test_is_valid))

    def test_min_stack():
        st = MinStack()
        st.push(-2)
        st.push(0)
        st.push(-3)
        assert st.getMin() == -3
        st.pop()
        assert st.top() == 0
        assert st.getMin() == -2
    tests.append(("2. MinStack", test_min_stack))

    def test_eval_rpn():
        assert sl.evalRPN(["2", "1", "+", "3", "*"]) == 9
        assert sl.evalRPN(["4", "13", "5", "/", "+"]) == 6
    tests.append(("3. evalRPN", test_eval_rpn))

    def test_generate_parenthesis():
        assert sorted(sl.generateParenthesis(3)) == sorted(
            ["((()))", "(()())", "(())()", "()(())", "()()()"]
        )
    tests.append(("4. generateParenthesis", test_generate_parenthesis))

    def test_daily_temperatures():
        assert sl.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
            1, 1, 4, 2, 1, 1, 0, 0
        ]
    tests.append(("5. dailyTemperatures", test_daily_temperatures))

    def test_car_fleet():
        assert sl.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
    tests.append(("6. carFleet", test_car_fleet))

    def test_largest_rectangle_area():
        assert sl.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    tests.append(("7. largestRectangleArea", test_largest_rectangle_area))

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
    s = "()[]{}"
    print(s)

    sl = Solution()
    # Call whichever method you're practicing, e.g.:
    # print(sl.isValid(s))

    print()
    run_tests()
