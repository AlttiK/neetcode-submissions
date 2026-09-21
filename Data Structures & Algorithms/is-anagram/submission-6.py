class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = dict()
        tDict = dict()

        for c in s:
            if c not in sDict:
                sDict.setdefault(c, 0)
            sDict[c] += 1
        
        for c in t:
            if c not in tDict:
                tDict.setdefault(c, 0)
            tDict[c] += 1
        
        return sDict == tDict
