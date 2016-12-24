## 442. Find All Duplicates in an Array

class Solution(object):
    def findDuplicates(self, nums):
        if len(nums) == 0:
            return []
            
        transfers = set()
        dupes = []
  
        for Int in nums:
            if Int not in transfers:
                transfers.add(Int)
            else:
            	dupes.append(Int)
                
        return dupes
