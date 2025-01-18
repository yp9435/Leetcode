from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Count how often each number appears
        count = defaultdict(int)
        for i in nums:
            count[i] += 1

        #Create buckets for numbers based on their frequency
        freq_bucket = [[] for i in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq_bucket[cnt].append(num)

        #Collect the top K frequent numbers starting from the highest frequency
        res = []
        for i in range(len(freq_bucket) - 1, 0, -1):  # Go through buckets from high to low
            for n in freq_bucket[i]:
                res.append(n)  # Add the number to the result
                if len(res) == k:  # Stop once we have k elements
                    return res
