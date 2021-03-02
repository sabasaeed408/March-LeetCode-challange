class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) //2, len(set(candyType)))
      //set kept the things which are unique in the list
        
