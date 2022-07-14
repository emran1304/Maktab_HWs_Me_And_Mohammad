def loop(n):
    print('loop{}'.format(n))
    if n >= 1:
        return loop(n-1)

loop(2)
