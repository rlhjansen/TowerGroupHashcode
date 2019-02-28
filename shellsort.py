from read_object import create_Image, create_slides, create_file
from random import randint



fa = "data/a_example.txt"
fb = "data/b_lovely_landscapes.txt"
fc = "data/c_memorable_moments.txt"
fd = "data/d_pet_pictures.txt"
fe = "data/e_shiny_selfies.txt"

files = [["a", fa], ["b", fb], ["c", fc], ["d", fd], ["e", fe]]
files = [f[1] for f in files]

class sorta_shellsort:
    def __init__(self, slides, dataset):
        self.slides = slides
        self.len = len(slides)
        self.dataset = dataset

    def scoring(self):
        self.score = sum([self.slides[i-1].score(elem) for i, elem in enumerate(self.slides)])

    def shellcompare(self, index, difference):
        s1, s2, s3, sd1 = index, index-1, index-2, index-difference
        sd2, sd3 = sd1-1, sd1-2
        current_1 = self.slides[s2].score(self.slides[s3]) + self.slides[s1].score(self.slides[s2])
        current_2 =  self.slides[sd2].score(self.slides[sd3]) + self.slides[sd1].score(self.slides[sd2])
        changed_1 = self.slides[sd2].score(self.slides[s3]) + self.slides[s1].score(self.slides[sd2])
        changed_2 =  self.slides[s2].score(self.slides[sd3]) + self.slides[sd1].score(self.slides[s2])
        current = current_1 + current_2
        changed = changed_1 + changed_2
        if changed > current:
            self.slides[s2], self.slides[sd2] = self.slides[sd2], self.slides[s2]
            self.unchanged = 0

    def run_alg(self, max_unchanged=100000):
        self.unchanged = 0
        interval = 5000
        iters = 0
        try:
            while self.unchanged < max_unchanged:
                self.unchanged += 1
                iters += 1
                start_ind, difference = randint(0, self.len-1), randint(0, 200)
                self.shellcompare(start_ind, difference)
                if not iters % interval:
                    self.scoring()
                    print("iters", iters)
                    print("score", self.score)
            self.scoring()
        except:
            create_file(self.slides, self.dataset+"_results.csv")

slides_b = create_slides(create_Image(fb))
ssssb = sorta_shellsort(slides_b, "b")
ssssb.run_alg()
print(ssssb.score)
