class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash=defaultdict(list)
        for st in strs:
            count=[0]*26 
            for i in range(len(st)):
                count[ord(st[i])-ord('a')]+=1
            hash[tuple(count)].append(st)
        
        return list(hash.values()) 
                



        
        