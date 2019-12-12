from LNode import SimpleLinkedList
linkedList = SimpleLinkedList()
linkedList.init_linked_list([1, 2, 3, 4,5,6,7,8,9,10])
linkedList

while end.next != None:
    i = 1
    while i <= k and end != None:
        end = end.next
        i += 1
    if end == None:
        break
    # 找到了每段翻转的结尾和开头, 并把结尾截断
    start = Pre.next
    Next = end.next
    end.next = None
    Pre.next = self.reverse_util(start)
    start.next = Next
    Pre = start
    end = Pre