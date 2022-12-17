# 1 determine the sequence formula, print the next number of sequence

user_seq = str(input("Enter a sequence of 4 or more numbers, separated by comma: "))


def func_seq(x):
    seq = list(map(int, x.split(",")))
    if f_1(seq):
        return f_1(seq)
    elif f_2(seq):
        return f_2(seq)
    elif f_3(seq):
        return f_3(seq)
    else:
        return -1


def f_1(seq):    # +x
    if seq[1] - seq[0] == seq[2] - seq[1] == seq[3] - seq[2] == seq[-1] - seq[-2]:
        step = seq[2] - seq[1]
        return seq[-1] + step
    else:
        return False


def f_2(seq):    # *x
    if seq[2] / seq[1] == seq[3] / seq[2] == seq[-1] / seq[-2]:
        step = seq[2] / seq[1]
        return seq[-1] * step
    else:
        return False


def f_3(seq):   # **x
    x = 2
    n = seq[0]
    while n in seq:
        if n ** x == seq[0] and (n + 1) ** x == seq[1] and (n + 2) ** x == seq[2] and (n + 3) ** x == seq[3]:
            return (len(seq) + 1) ** x
        else:
            x += 1
            if x == 10:
                return False


print(func_seq(user_seq))

# 2 find the largest palindrome, created by multiplying three-digit numbers

def palindrome(x):
    x_str = list(str(x))
    if x_str[::-1] == x_str:
        return x


def max_multiply_palindrome(a, b):
    """
    :param a: the largest number of the range of multipliers
    :param b: the smallest number of the range of multipliers
    :return: the largest palindrome, created by multiplying numbers of the range, multipliers
    """
    res = 0
    res_a = 0
    res_b = 0
    for j in range(a, (b - 1), -1):
        for i in range(a, (b - 1), -1):
            if j * i > res:
                if palindrome(j * i):
                    res = j * i
                    res_a = j
                    res_b = i
    return res, res_a, res_b


print(max_multiply_palindrome(999, 100))
