class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a1=list(s)
        a2=list(t)
        freq1=Counter(a1)
        freq2=Counter(a2)
        if freq1==freq2:
            return True
        return False
        