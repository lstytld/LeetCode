class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        if not houses: return None
        houses.sort()
        heaters.sort()
        max_dis = 0
        prev_heater = float("-inf")
        index_house = 0
        for heater in (heaters + [float("inf")]):
            cur_heater = heater
            while index_house < len(houses) and houses[index_house] <= cur_heater:
                max_dis = max(max_dis, min(houses[index_house] - prev_heater, cur_heater - houses[index_house]))
                index_house += 1
            prev_heater = cur_heater
        return max_dis

