class NumArray(object):

    def __init__(self, nums):
        nums_array = nums

        pxsum = []
        pxsum.append(nums_array[0])

        for i in range(1, len(nums_array)):
            pxsum.append(pxsum[i - 1] + nums_array[i])

        self.pxsum = pxsum

    def sumRange(self, left, right):
        if left == 0:
            return self.pxsum[right]

        return self.pxsum[right] - self.pxsum[left - 1]