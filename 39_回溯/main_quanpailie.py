# 用回溯的办法写出 数组的全排列

array = [1, 2, 3]
result = []

def backtrace(array, current_path):
    global result
    # 如果target的的长度等于 array的长度
    if len(current_path) == len(array):
        # result.append(current_path)
        print(current_path)
        return

    # 如果长度不满足 那么继续添加

    for i in array:
        # 如果字符在当前路径中 那么不遍历
        if i in current_path:
            continue
        # 如果该字符不在当前路径中 加入到当前路径
        current_path.append(i)
        backtrace(array, current_path)
        current_path.pop()


current_path = []
backtrace(array, current_path)
print(result)


