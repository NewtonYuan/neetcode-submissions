class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = [[strs[0]]]
        for s in range(1, len(strs)):
            found = False
            for i in range(len(res)):
                if sorted(strs[s]) == sorted(res[i][0]):
                    res[i].append(strs[s])
                    found = True
                    break
            if not found:
                res.append([strs[s]])
        return res
                
        