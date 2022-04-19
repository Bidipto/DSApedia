# 49. Group Anagrams
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    dic = defaultdict(list)
    for i in strs:
        dic["".join(sorted(list(i)))].append(i)
    return dic.values()