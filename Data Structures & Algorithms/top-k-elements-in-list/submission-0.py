class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        sorted_dict = sorted(
            frequency.items(),
            key=lambda item: item[1],
            reverse=True
        )

        res = []

        for i in range(k):
            res.append(sorted_dict[i][0])

        return res