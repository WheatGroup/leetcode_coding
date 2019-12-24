# 多线程
import threading
from threading import Lock
class FooBar:
    def __init__(self, n):
        self.n = n
        # 想交叉顺序的话 必须的两个锁了 一个锁只能保证是foofoobarbar
        self.locks = [Lock(), Lock()]
        # 其实这个锁的设定 也是尝试出来的
        self.locks[1].acquire()


    def foo(self):
        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.locks[0].acquire()
            print('Foo')
            self.locks[1].release()


    def bar(self) -> None:
        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.locks[1].acquire()
            print('Bar')
            self.locks[0].release()


foobar = FooBar(4)
th1 = threading.Thread(target=foobar.foo)
th2 = threading.Thread(target=foobar.bar)
th1.start()
th2.start()
th1.join()
th2.join()