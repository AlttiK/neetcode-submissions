class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for st in strs:
            alph_order = ''.join(sorted(st))
            anagram_dict[alph_order].append(st)
        return list(anagram_dict.values())
