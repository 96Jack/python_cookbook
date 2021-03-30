"""
q：  对期末成绩，去掉最高分和最低分，保留中间的成绩
"""

def drop_first_last(grades):
    first , *middle, last = grades
    print(middle)
    return avg(middle)

def avg(mid):
    return sum(mid)/len(mid)


grades = [100, 93, 94, 96, 97, 88, 77, 66, 55, 33, 0]
print(drop_first_last(grades))
