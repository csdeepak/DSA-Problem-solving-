class Solution(object):
    def carPooling(self, trips, capacity):
        for i in range(len(trips)-1):
            if trips[i][0]+trips[i+1][0]>capacity and trips[i][2]<trips[i+1][2]:
                return False
                break
        return True       