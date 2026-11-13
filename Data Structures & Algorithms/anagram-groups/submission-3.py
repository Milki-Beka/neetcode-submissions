class Solution:

  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # groups = []
    # if len(strs) == 0:
    #   return []
    # if len(strs) == 1:
    #   return [strs]
    # for i in range(len(strs)):
    #     if strs[i] is None:
    #         continue
    #     current_group = [strs[i]]
    #     for j in range(i + 1, len(strs)):
    #         if strs[j] is not None and Counter(strs[i]) == Counter(strs[j]):
    #             current_group.append(strs[j]) 
    #             strs[j] = None 
    #     groups.append(current_group)
    # return groups

    bins = {}
    for word in strs:
        ww = "".join(sorted(word))
        if ww not in bins:
            bins[ww] = []
        bins[ww].append(word)
    return list(bins.values())