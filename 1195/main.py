import threading
from threading import Semaphore
sem = Semaphore()
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.i = 1

    # printFizz() outputs "fizz"
    def fizz(self) -> None:
        while(self.i <= self.n):
            if self.i % 3 == 0 and self.i % 5 != 0:
                sem.acquire()
                print('fizz')
                self.i += 1
                sem.release()

    def buzz(self) -> None:
        while (self.i <= self.n):
            if self.i % 5 == 0 and self.i % 3 != 0:
                sem.acquire()
                print('buzz')
                self.i += 1
                sem.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self) -> None:
        while (self.i <= self.n):
            if self.i % 5 == 0 and self.i % 3 == 0:
                sem.acquire()
                print('fizzbuzz')
                self.i += 1
                sem.release()
    # printNumber(x) outputs "x", where x is an integer.
    def number(self) -> None:
        while (self.i <= self.n):
            if self.i % 5 != 0 and self.i % 3 != 0:
                sem.acquire()
                print(self.i)
                self.i += 1
                sem.release()


fizzbuzz = FizzBuzz(15)
th1 = threading.Thread(target=fizzbuzz.fizz)
th2 = threading.Thread(target=fizzbuzz.buzz)
th3 = threading.Thread(target=fizzbuzz.fizzbuzz)
th4 = threading.Thread(target=fizzbuzz.number)

th1.start()
th2.start()
th3.start()
th4.start()

th1.join()
th2.join()
th3.join()
th4.join()
