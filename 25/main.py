from LNode import LNode, SimpleLinkedList
linkedList = SimpleLinkedList()
linkedList.init_linked_list([2, 1, 3, 6, 5, 8, 9, 7])
linkedList.print_all()
print('')
def print_link(head):
    while head.next != None:
        print(str(head.next.data), end=',')
        head = head.next
    print('')


def merge_sort(head):
    # 至少保证有两个结点 才能进行归并
    if head.next == None or head.next.next == None:
        return head
    fast = head
    slow = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next

    link1 = head
    link2 = LNode(0)
    link2.next = slow.next
    slow.next = None
    left = merge_sort(link1)
    right = merge_sort(link2)

    # 对返回的两个链表进行排序
    head = res = LNode(0)
    left = left.next
    right = right.next
    while left != None and right != None:
        if left.data <= right.data:
            head.next = left
            left = left.next
        else:
            head.next = right
            right = right.next
        head = head.next

    if left == None:
        head.next = right
    else:
        head.next = left

    return res

link_head = linkedList.get_head()
res = merge_sort(link_head)
linkedList.set_head(res)
linkedList.print_all()
















