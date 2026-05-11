from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)
        for string in strs:
            str_map[''.join(sorted(string))].append(string)
        return list(str_map.values())