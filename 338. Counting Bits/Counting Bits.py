# @author:leacoder 
# @des: 比特位计数
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num + 1)
        for i in range(1,num+1):
            res[i] = res[i&(i-1)] + 1
        return res  