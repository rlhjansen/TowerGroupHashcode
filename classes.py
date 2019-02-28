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
        """Returns number of tags that are in both images"""
        return len(self.tags & other.tags)

    def __sub__(self, other):
        """Returns minimum number of tags exclusively in one image """
        return min(len(self.tags - other.tags), len(other.tags - self.tags))


# class slide:

#     def __init__(self):
#         self.filled = False
#         self.images = []

#     def insert(self, image):
#         """Returns True if success, False if incompatible"""

#         if not self.filled:
#             if self.images:
#                 if image.orientation == 'V':
#                     self.images.append(image)
#                     self.filled = True
#                 else:
#                     return False
#             else:
#                 self.images.append(image)
#                     if image.orientation == 'H':
#                         self.filled = True
#             return True

#     def remove(self, image):
#         """Returns the popped image"""
#         self.images.remove(image)
#         self.filled = False
#         return image
