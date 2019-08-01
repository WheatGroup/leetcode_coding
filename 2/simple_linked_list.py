#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""

@version: 0.1
@author:  admin
@email:   wangrui0810@gmail.com
@file:    simple_linked_list.py
@time:    2019/8/1 15:40
"""
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
        self.__head = None

    '''头插法'''
    def insert_to_head(self, value):
        lnode = LNode(value)
        # 能这么调用next函数赋值 是因为 @data.setter
        lnode.next = self.__head
        self.__head = lnode

    def print_all(self):
        pos = self.__head
        if pos == None:
            print('空链表')
            return
        while pos.next != None:
            # end参数默认是换行符
            print(str(pos.data) + '-->', end='')
            pos = pos.next
        print(str(pos.data))

    def init_linked_list(self, values, if_reversed=False):
        if if_reversed:
            for i in values:
                self.insert_to_head(i)
        else:
            for i in reversed(values):
                self.insert_to_head(i)


if __name__ == "__main__":
    linkedList = SimpleLinkedList()
    linkedList.init_linked_list([1,2,3,4])
    linkedList.print_all()