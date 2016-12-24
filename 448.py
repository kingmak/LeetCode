## 448. Find All Numbers Disappeared in an Array

class Solution(object):
    def findDisappearedNumbers(self, nums):
        if len(nums) == 0:
            return []
            
        singleSorted = list(set(sorted(nums)))
        maxed = range(singleSorted[0], len(nums) + 1)
        notIn = []
        
        for Int in maxed:
            if Int not in singleSorted:
                notIn.append(Int)
                
        return notIn
