#利用优先级队列完成 本质就是一个二叉堆
# 完成一次二叉堆的建堆操作 也就实现了优先级的排序
# 出现的次数越高 优先级越高
# 用哈希表存储每个元素出现的次数
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        heap = []
        cnt_dict = dict(Counter(nums))
        fre_key = {}
        # 开始按照哈希表 进行建堆  每插入一个元素进入堆中的时间复杂度是o(lgK)
        for key, value in cnt_dict.items():
            fre_key[value] = key
        for freq in fre_key.keys():
            freq = -freq
            heapq.heappush(heap, freq)
        result = []
        print(heap)
        for i in range(0, k):
            temp = heapq.heappop(heap)
            temp = -temp
            result.append(fre_key[temp])
        print(result)

s = Solution()
nums = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd']
k = 2
s.topKFrequent(nums, k)
