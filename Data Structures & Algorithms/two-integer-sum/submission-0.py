class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    if i < j:
                        return [i , j]
                        break
                    else:
                        return [j , i]
                        break
        