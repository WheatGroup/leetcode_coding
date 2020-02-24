# 阶乘
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


num = factorial(5)
print(num)

'''
一只青蛙可以一次跳 1 级台阶或一次跳 2 级台阶,例如:
跳上第 1 级台阶只有一种跳法：直接跳 1 级即可。跳上第 2 级台阶
有两种跳法：每次跳 1 级，跳两次；或者一次跳 2 级。
问要跳上第 n 级台阶有多少种跳法？
'''

def jump(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return jump(n-1) + jump(n-2)

res = jump(10)
print(res)