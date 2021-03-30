"""
对于分解未知长度的叠代表对象，利用*表达式分解
"""

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3,4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    print(tag)
    # print(*args)
    # if tag == 'foo':
    #     do_foo(*args)
    # elif tag == 'bar':
    #     do_bar(*args)

    
