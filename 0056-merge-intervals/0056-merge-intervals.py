class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals) # size of the array
        arr = intervals
        # sort the given intervals:
        arr.sort()

        ans = []

        for i in range(n):
            # if the current interval does not
            # lie in the last interval:
            if not ans or arr[i][0] > ans[-1][1]:
                ans.append(arr[i])
            # if the current interval
            # lies in the last interval:
            else:
                ans[-1][1] = max(ans[-1][1], arr[i][1])
        return ans
        