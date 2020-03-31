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
        # 有头结点
        self.__head = LNode(0)
        self.__head.next = None

    def init_linked_list(self, values):
        for i in reversed(values):
            self.insert_to_head(i)

    def insert_to_head(self, value):
        lnode = LNode(value)
        lnode.next = self.__head.next
        self.__head.next = lnode

    def recursive(self, tail, p):
        if p == None:
            return
        # 先让p的前一个节点和p的后一个节点连上
        pre.next = p.next
        # 将p进行头插法
        q = self.__head.next
        self.__head.next = p
        p.next = q
        pre = pre.next
        self.print_all()
        self.recursive(p)

    def reverse_linked_node(self):
        # 用递归的办法
        # 假设链表至少有两个节点
        self.recursive(self.__head.next, self.__head.next.next)

    def print_all(self):
        current = self.__head.next
        while (current != None):
            print(str(current.data) + ' ', end='')
            current = current.next
        return



if __name__ == "__main__":
    # 初始化单链表
    input = "1->2->3->4->5->NULL"
    num_list = input.split('->')[0:-1]
    linkedList = SimpleLinkedList()
    linkedList.init_linked_list(num_list)
    linkedList.print_all()
    print('---------------')
    linkedList.reverse_linked_node()
    linkedList.print_all()

