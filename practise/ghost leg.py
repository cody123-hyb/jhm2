def ghost_leg(a):
    b = list(range(len(a[0]) // 2 + 1))
    for a in a:
        for i in range(len(a) // 2):
            if a[2*i+1] == '-':
                b[i], b[i+1] = b[i+1], b[i]
    return b

a = [
    '|-| |',
    '| |-|',
    '|-| |',
    '| | |'
]

b = ghost_leg(a)
print("最终的结果顺序是:", b)
