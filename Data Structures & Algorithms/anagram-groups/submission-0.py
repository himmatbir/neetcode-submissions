class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap: dict[str, List[str]]={}
        for str in strs:
            sortedStr= "".join(sorted(str))
            anagramMap.setdefault(sortedStr, []).append(str)
        return list(anagramMap.values())