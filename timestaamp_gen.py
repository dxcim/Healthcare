def timegen:
    h = m = s = 0

    while h < 4:
        print("{}:{}:{}".format(h, m, s))
        s += 1
        if s == 60:
            s = 00
            m += 1
        if m == 60:
            m = 00
            h += 1