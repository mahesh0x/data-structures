# NeetCode 150 — Advanced Graphs
# No shared helper module: inputs are weighted edge lists, coordinate lists, and
# grids that differ per problem, so each test builds its sample input inline.
from typing import List


class Solution:
    # 1. Reconstruct Itinerary
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        pass

    # 2. Min Cost to Connect All Points
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pass

    # 3. Network Delay Time
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pass

    # 4. Swim in Rising Water
    def swimInWater(self, grid: List[List[int]]) -> int:
        pass

    # 5. Foreign Dictionary (Alien Dictionary)
    def foreignDictionary(self, words: List[str]) -> str:
        pass

    # 6. Cheapest Flights Within K Stops
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        pass


def run_tests():
    sl = Solution()
    tests = []

    def test_find_itinerary():
        tickets = [
            ["MUC", "LHR"],
            ["JFK", "MUC"],
            ["SFO", "SJC"],
            ["LHR", "SFO"],
        ]
        assert sl.findItinerary(tickets) == ["JFK", "MUC", "LHR", "SFO", "SJC"]
    tests.append(("1. findItinerary", test_find_itinerary))

    def test_min_cost_connect_points():
        points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
        assert sl.minCostConnectPoints(points) == 20
    tests.append(("2. minCostConnectPoints", test_min_cost_connect_points))

    def test_network_delay_time():
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        assert sl.networkDelayTime(times, 4, 2) == 2
    tests.append(("3. networkDelayTime", test_network_delay_time))

    def test_swim_in_water():
        grid = [
            [0, 2],
            [1, 3],
        ]
        assert sl.swimInWater(grid) == 3
    tests.append(("4. swimInWater", test_swim_in_water))

    def test_foreign_dictionary():
        # derived total order is unique here: w < e < r < t < f
        assert sl.foreignDictionary(["wrt", "wrf", "er", "ett", "rftt"]) == "wertf"
    tests.append(("5. foreignDictionary", test_foreign_dictionary))

    def test_find_cheapest_price():
        flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
        assert sl.findCheapestPrice(4, flights, 0, 3, 1) == 700
    tests.append(("6. findCheapestPrice", test_find_cheapest_price))

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
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    print("network (u -> v, weight):", times)

    sl = Solution()
    # Call whichever method you're practicing, e.g.:
    # print(sl.networkDelayTime(times, 4, 2))

    print()
    run_tests()
