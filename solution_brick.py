import math

# TODO: class that creates a rectangle on the canvas from the generator output
# TODO: a parent class which holds the canvas for resizing it?

class Brick:
    def __init__(self, text):

    def __len__(self):
        return math.floor(math.log10(int(self.text)))
