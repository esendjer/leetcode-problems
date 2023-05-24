# Try to rewrite all the code from scratch in vi/vim
# or in any simple text editor
import heapq
class KthLargest:

    def __init__(self, k: int, nums):
        self.nums = []
        self.k = k
        for i in nums:
            self.add(i)
    
    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        else:
            if self.nums[0] < val:
                heapq.heappushpop(self.nums, val)
        return self.nums[0]

    
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

cases = (
    # ["KthLargest","add","add","add","add","add"],
    [[3,[4,5,8,2]],[3],[5],[10],[9],[4]],
)
for i in cases:
    obj = KthLargest(*i[0])
    for v in i[1:]:
        param_1 = obj.add(v[0])
        print(param_1)