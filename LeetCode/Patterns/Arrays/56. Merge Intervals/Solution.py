class Solution(object):

    def merge(self, intervals):

        intervals.sort(key=lambda iv: iv[0])

        merge = [list(intervals[0])]

        for start, end in intervals[1:]:

            if start <= merge[-1][1]:
                merge[-1][1] = max(merge[-1][1], end)

            else:
                merge.append([start, end])

        return merge