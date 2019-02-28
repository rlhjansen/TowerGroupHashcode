from collections import Counter
import matplotlib.pyplot as plt

fa = "data/a_example.txt"
fb = "data/b_lovely_landscapes.txt"
fc = "data/c_memorable_moments.txt"
fd = "data/d_pet_pictures.txt"
fe = "data/e_shiny_selfies.txt"

files = [["a", fa], ["b", fb], ["c", fc], ["d", fd], ["e", fe]]

def distr(file):
    c = Counter()
    f = open(file)
    for line in f.readlines():
        c.update(read_tags(line))
    return c


def read_tags(line):
    return line.split(" ")[2:]


def lprint(iterable):
    for elem in iterable:
        print(elem)

for f in files:
    values = Counter([v for v in distr(f[1]).values()]).most_common()
    xs = [v[1] for v in values]
    ys = [v[0] for v in values]
    plt.plot(xs, ys)
    plt.yscale("log")
    plt.title(f[0])
    plt.ylabel("occurance of tag")
    plt.xlabel("occurance of occurance")
    plt.show()
