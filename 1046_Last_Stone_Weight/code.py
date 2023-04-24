class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) != 1:
            stones = sorted(stones)[::-1]
            st1 = stones.pop(0)
            st2 = stones.pop(0)

            stones.append(abs(st1 - st2))
        
        return stones[0]
