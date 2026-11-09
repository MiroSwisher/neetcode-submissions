class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seenAnagrams = {}

        for s in strs:
            key = str(sorted(s))
            if key not in seenAnagrams:
                seenAnagrams[key] = [s]
            else:
                seenAnagrams[key].append(s)
        
        return list(seenAnagrams.values())