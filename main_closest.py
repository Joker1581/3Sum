from typing import List
import time
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(res - target):
                    res = s
                if s == target:
                    return target
                elif s < target:
                    l += 1
                else:
                    r -= 1
        return res
if __name__ == "__main__":
    start_time = time.time()
    print(Solution.threeSumClosest(Solution, [-1,2,1,-4], 1))
    end_time = time.time()
    print('cost %f second' % (end_time - start_time))