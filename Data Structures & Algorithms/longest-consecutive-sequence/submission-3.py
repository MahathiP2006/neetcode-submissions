class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash=set(nums)
        max_len=0
        for val in nums:
            if (val-1) not in hash:
                length=0
                while(val+length) in hash:
                    length+=1
                max_len=max(max_len,length)

        return max_len