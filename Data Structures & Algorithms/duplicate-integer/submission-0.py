class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a set hashmap which will reduce time complexity to O(n)
        hashmap = set()

        for num in nums:
            if num in hashmap:
                return True
            
            hashmap.add(num)

        return False
        