import read_object as ro


class Image:
    """Image class
       properties:

            id (int): identifier number.
            orientation (char): 'H' for horizontal 'V' for vertical.
            tags (set): set containing the tags of the image.
    """

    def __init__(self, id, orientation, tags):
        self.id = id
        self.orientation = orientation
        self.tags = set(tags)

    def __add__(self, other):
        """Return tags in both images"""
        return self.tags | other.tags

    def __str__(self):
        return self.orientation + ' ' + str(self.tags)

    # def __sub__(self, other):
    #     """Returns minimum number of tags exclusively in one image """
    #     return min(len(self.tags - other.tags), len(other.tags - self.tags))


class slide:

    def __init__(self):
        self.filled = False
        self.images = []

    def insert(self, image):
        """Returns True if success, False if incompatible"""

        if not self.filled:
            if self.images:
                if image.orientation == 'V':
                    self.images.append(image)
                    self.filled = True
                else:
                    return False
            else:
                self.images.append(image)
                if image.orientation == 'H':
                    self.filled = True
            return True

    def remove(self, image):
        """Returns the popped image"""

        self.images.remove(image)
        self.filled = False
        return image

    def tags(self):
        """returns all tags in slide """

        if self.filled:
            if len(self.images) == 2:
                return self.images[0] + self.images[1]
            else:
                return self.images[0].tags
        else:
            return set()

    def score(self, next):
        """Returns the score of a slide progression"""
        return min(len(self.tags() - other.tags()), len(other.tags() - self.tags()), len(other.tags() & self.tags()))


if __name__ == '__main__':
    file_name = "data/e_shiny_selfies.txt"
    imgs = ro.create_Image(file_name)
    print(imgs[0], imgs[1], imgs[2])
