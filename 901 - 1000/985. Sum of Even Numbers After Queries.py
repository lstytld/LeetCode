class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        start = 0
        for i in A:
            if i % 2 == 0:
                start += i
        for value, index in queries:
            if A[index] % 2 == 0:
                if value % 2 == 0:
                    start += value
                else:
                    start -= A[index]
            else:
                if value % 2 == 1:
                    start += A[index] + value
            A[index] += value
            ans.append(start)
        return ans
