class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram = {}

        for s in strs:
            key = tuple(sorted(s))


            if key not in anagram:
                anagram[key] = [s]
            else:
                anagram[key].append(s)

        return anagram.values()
