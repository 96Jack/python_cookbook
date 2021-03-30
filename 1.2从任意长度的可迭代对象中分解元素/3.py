"""
递归求序列的和
"""
items = [1, 10, 7, 4, 5, 9]

def sum(items):
    head, *tail = items
    print(head)
    print(*tail)
    return head + sum(tail) if tail else head


# print(sum(items))
sum(items)

