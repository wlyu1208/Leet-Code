class Solution:
    def merge(self, left, right):
        res = []
        while len(left) != 0 and len(right)!= 0:
            if left[0] < right[0]:
                res.append(left[0])
                left.remove(left[0])
            else:
                res.append(right[0])
                right.remove(right[0])
            
        if len(left) == 0:
            res = res + right
        else:
            res = res + left
        
        return res
    
    def merge_sort(self, unsort):
        if len(unsort) <= 1:
            return unsort
        mid = len(unsort) // 2
        left = unsort[:mid]
        right = unsort[mid:]
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        return list(self.merge(left, right))
    
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq_num = [num ** 2 for num in nums]
        answer = self.merge_sort(sq_num)
        
        
        return answer
                
