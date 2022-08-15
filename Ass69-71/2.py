for v in range(1, 100):
    my_range = list(range(v))
    x = sum(my_range, v) + pow(v, v, v)
    if x != 820:
        my_range.clear()
    else:
        print(v)
