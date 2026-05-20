class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))

            if key not in res:
                res[key] = []

            res[key].append(strs[i])

        return list(res.values())