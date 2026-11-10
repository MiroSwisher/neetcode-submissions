class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        for n in nums:
            if n not in num_count:
                num_count[n] = 1
            else:
                num_count[n] += 1
        
        pairs = []
        for n in num_count:
            pairs.append([n, num_count[n]])
        
        sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)

        top_k = []

        for i in range(k):
            top_k.append(sorted_pairs[i][0])
        
        return top_k