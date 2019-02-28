class Image:
    """Image class
       properties:

            orientation (char): 'H' for horizontal 'V' for vertical
            tags (set): set containing the tags of the image
            """

    def __init__(self, id, orientation, tags):
        self.id = id
        self.orientation = orientation
        self.tags = set(tags)

    def __add__(self, other):
        """Returns number of tags that are in both images"""
        return len(self.tags & other.tags)

    def __sub__(self, other):
        """Returns minimum number of tags exclusively in one image """
        return min(len(self.tags - other.tags), len(other.tags - self.tags))
