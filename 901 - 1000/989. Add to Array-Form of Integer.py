class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        ans = []
        flag = 0
        i = 1
        while (i <= len(A) or K > 0) or flag == 1:
            A_num = A[-i] if i <= len(A) else 0
            K_num = K % 10
            num_sum = K_num + A_num + flag
            ans.append(num_sum % 10)
            flag = num_sum // 10
            K = K // 10
            i += 1

        return ans[::-1]
