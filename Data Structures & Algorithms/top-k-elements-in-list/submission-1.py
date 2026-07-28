from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        sorted_key= sorted(set(nums), key= lambda x : (-dic[x],x))
        return sorted_key[:k]

        
        