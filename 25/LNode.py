class LNode(object):
    def __init__(self, data, next=None):
        # 私有变量用双下划线开头
        self.__data = data
        self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next


class SimpleLinkedList(object):
    '''单链表'''
    def __init__(self):
        self.__head = LNode(0)
        self.__head.next = None


    def init_linked_list(self, values, if_reversed=False):
        if if_reversed:
            for i in values:
                self.insert_to_head(i)
        else:
            for i in reversed(values):
                self.insert_to_head(i)


    def insert_to_head(self, value):
        lnode = LNode(value)
        lnode.next = self.__head.next
        self.__head.next = lnode

    def print_all(self):
        current = self.__head.next
        while(current != None):
            print(str(current.data) + ' ', end='')
            current = current.next
        return

    def linked_list_count(self):
        count = 0
        current = self.__head.next
        while(current != None):
            count += 1
            current = current.next
        return count


    def reverse_util(self, start):
        # 翻转这段区间的链表 然后返回值是这段链表的第一个结点和最后一个结点
        pre = None
        curr = start
        while curr != None:
            Next = curr.next
            curr.next = pre
            pre = curr
            curr = Next
        return pre



    def reverse_linked_list(self, k):
        # 把链表每num个 翻转一次
        Pre = self.__head
        end = self.__head
        if k > self.linked_list_count():
            self.print_all()
        else:
            # 先遍历k次 查找到每段的头和尾
            while end.next != None:
                i = 0
                while i < k and end != None:
                    end = end.next
                    i = i + 1
                if end == None:
                    break
                Next = end.next
                start = Pre.next
                end.next = None
                Pre.next = self.reverse_util(start)
                start.next = Next
                end = start
                Pre = start
        return


if __name__ == "__main__":
    linkedList = SimpleLinkedList()
    linkedList.init_linked_list([1,2,3,4,5,6,7,8,9,10])
    linkedList.print_all()
    cnt = linkedList.linked_list_count()
    print('')
    # print(cnt)
    linkedList.reverse_linked_list(3)
    linkedList.print_all()
    # 如果链表的节点数少于k 那么打印整个链表