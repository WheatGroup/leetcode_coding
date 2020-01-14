'''
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
'''

def num_decode(s):
    length = len(s) - 1
    return decode(s, length)


def decode(s, index):
    if (index <= 0):
        return 1
    # 解码数和两部分有关 curr和 prev+curr
    # 当前字符和前一个字符
    curr = s[index]
    prev = s[index-1]

    if curr == '0':
        count = 0

    else:
        count = decode(s, index-1)

    # 除了自身的次数 还需要加上与前一个字符连一块次数
    if (prev == '2' and curr <= '6') or (prev == '1'):
        count += decode(s, index-2)

    return count


cnt = num_decode('26')
print(cnt)






