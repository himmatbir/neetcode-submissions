class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charMap:dict[str, int]= {}
        for c in s:
            charMap[c]= charMap.get(c, 0)+1

        for c in t:
            if c in charMap:
                if charMap[c]==1:
                    charMap.pop(c)
                else:
                    charMap[c]= charMap.get(c) - 1
            else:
                return False
        return not len(charMap)>0
        
        

        