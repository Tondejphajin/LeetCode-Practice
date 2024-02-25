from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        next_step_cost = 0
        next_next_step_cost = 0

        for i in range(len(cost) - 1, -1, -1):
            current_step_cost = cost[i] + min(next_step_cost, next_next_step_cost)

            next_next_step_cost = next_step_cost
            next_step_cost = current_step_cost

        return min(next_step_cost, next_next_step_cost)
