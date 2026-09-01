class Solution(object):

    def insert(self, intervals, newInterval):

        intervals.append(newInterval)

        intervals.sort(key=lambda iv: iv[0])

        merge = [intervals[0]]

        for start, end in intervals[1:]:

            if start <= merge[-1][1]:
                merge[-1][1] = max(merge[-1][1], end)

            else:
                merge.append([start, end])

        return merge