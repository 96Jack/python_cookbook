"""
q: 输出文本匹配行，及输出当前文本匹配行以前最后检查过的N 行文本
"""

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == "__main__" :
     with open('1.txt') as f :
        for line, previous_lines in search(f , "python", 5):
            for pline in previous_lines:
                print(pline, end="")
            print(line, end="")
            print("-"*20)