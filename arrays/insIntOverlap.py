class Solution:
    def insertInterval(self, intervals, new):
        ans = []
        i = 0
        n = len(intervals)

        # Add all intervals before `new` starts
        while i < n and intervals[i][1] < new[0]:
            ans.append(intervals[i])
            i += 1

        # Merge overlapping intervals with `new`
        while i < n and intervals[i][0] <= new[1]:
            new[0] = min(new[0], intervals[i][0])
            new[1] = max(new[1], intervals[i][1])
            i += 1
        ans.append(new)

        # Add all remaining intervals after `new`
        while i < n:
            ans.append(intervals[i])
            i += 1

        return ans
