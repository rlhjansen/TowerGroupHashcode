from collections import Counter

f = open("data/a_example.txt", "r")

f2 = open("data/b_lovely_landscapes.txt")


c = Counter()

def read_tags(line):
    return line.split(" ")[2:]

for line in f2.readlines():
    c.update(read_tags(line))


def lprint(iterable):
    for elem in iterable:
        print(elem)


lprint(c.most_common()[:20])
