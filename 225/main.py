from queue import Queue
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = Queue()
        self.q2 = Queue()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.put(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        # 始终保证是q1装的数据
        while(self.q1.qsize() > 1):
            temp_num = self.q1.get()
            self.q2.put(temp_num)

        num = self.q1.get()
        while(not self.q2.empty()):
            temp_num = self.q2.get()
            self.q1.put(temp_num)

        return num



    def top(self) -> int:
        """
        Get the top element.
        """
        num = self.pop()
        self.q1.put(num)
        return num




    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.q1.empty()



# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
print(param_2)
param_3 = obj.top()
print(param_3)
param_4 = obj.empty()
print(param_4)