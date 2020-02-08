class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2 == 1:
            return []
        total_jumbo = tomatoSlices//2 - cheeseSlices
        total_small = 2 * cheeseSlices - tomatoSlices//2
        if total_jumbo < 0 or total_small < 0:
            return []
        return [total_jumbo, total_small]