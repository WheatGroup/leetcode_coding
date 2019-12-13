# 利用栈完成 并用字典存储下标
class Stack(object):

    def __init__(self):
     # 创建空列表实现栈
        self.__list = []

    def is_empty(self):
    # 判断是否为空
        return self.__list == []

    def push(self,item):
    # 压栈，添加元素
        self.__list.append(item)

    def pop(self):
    # 弹栈，弹出最后压入栈的元素
        if self.is_empty():
            return
        else:
            return self.__list.pop()

    def top(self):
    # 取最后压入栈的元素
        if self.is_empty():
            return
        else:
            return self.__list[-1]

class Solution:
    def dailyTemperature(self, T):
        # 利用栈
        n_len = len(T)
        result = [0 for n in range(0, n_len)]
        stack = Stack()
        for i in range(0, n_len):
            node = {}
            node['index'] = i
            node['value'] = T[i]
            if stack.is_empty():
                stack.push(node)
            else:
                top = stack.top()
                while not stack.is_empty() and T[i] > top['value']:
                    top = stack.pop()
                    # 获取栈顶节点的下标
                    j = top['index']
                    result[j] = i - j
                    top = stack.top()
                stack.push(node)
        return result



s = Solution()
res = s.dailyTemperature([73, 74, 75, 71, 69, 72, 76, 73])
print(res)












