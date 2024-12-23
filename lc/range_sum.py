class NumArray:
    """ range sum """

    def __init__(self, nums: list[int]):
        self.nums = nums 
        self.nums_len = len(nums)
        self.sum = (self.nums_len + 1) * [0] 
        self.sum_back = (self.nums_len + 1) * [0] 

    def sumRange(self, left: int, right: int) -> int:
        for i in range(self.nums_len):
            self.sum[i+1] = self.sum[i] + self.nums[i]
        i = self.nums_len - 1
        while i >= 0:
            self.sum_back[i] = self.sum_back[i+1] + self.nums[i]
            i -= 1
        return self.sum[right+1] - self.sum[left]


# Your NumArray object will be instantiated and called as such:
obj = NumArray([1, 2, 3, 4, 5])
param_1 = print(obj.sumRange(2, 3))