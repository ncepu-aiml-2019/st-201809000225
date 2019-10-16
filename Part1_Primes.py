


if __name__ == '__main__':
    n = (int)(input("输入大于0数字，输出0到该数字之间的素数"))
    print(" ".join("%s" % x for x in range(2, n) if not [y for y in range(2, x) if x % y == 0]))
