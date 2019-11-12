def cal_correct(k, s, b):
    return pow(pow(k, 1 / b) + pow(s, 1 / b), b)


def cal_my(k, s, b):
    return k * pow(1 + pow(k / s, -1 / b), b - 1) + s * pow(1 + pow(k / s, 1 / b), b - 1)


k = 3
b = 0.4
s = 2

end = None
