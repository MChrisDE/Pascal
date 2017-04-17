import math


# TODO: class that creates a rectangle on the canvas from the generator output
# TODO: a parent class which holds the canvas for resizing it?


class Brick:
    def __init__(self, canvas, text, tempwidth, tempheight):
        self.text = text
        self.font_size = int(-7.500 * len(str(self.text)) + 37)
        canvas.create_rectangle(tempwidth - 25, tempheight - 25, tempwidth + 25, tempheight + 25, fill="white")
        canvas.create_text(tempwidth, tempheight, text=self.text, font=("Roboto", self.font_size))
