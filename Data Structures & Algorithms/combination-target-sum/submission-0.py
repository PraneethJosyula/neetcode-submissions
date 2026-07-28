class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(i, cur, tot):
            if tot == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or tot >  target:
                return
            cur.append(nums[i])
            backtrack(i, cur, tot+nums[i])
            cur.pop()
            backtrack(i+1, cur, tot)
        backtrack(0,[],0)
        return res

