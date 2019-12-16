import heapq
#  切记 堆一定是满二叉树
data = [97, 38, 27, 50, 76, 65, 49, 13]
heap = []

for n in data:
    heapq.heappush(heap, n)


print('pop:', heapq.heappop(heap))
print(heap)
print('pop:', heapq.heappop(heap))
print(heap)