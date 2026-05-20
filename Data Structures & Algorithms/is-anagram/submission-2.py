class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_occurances = {}
        t_occurances = {}
        for char in s:
            s_occurances[char] = s_occurances.get(char, 0) + 1
        for char in t:
            t_occurances[char] = t_occurances.get(char, 0) + 1
        return s_occurances == t_occurances
        