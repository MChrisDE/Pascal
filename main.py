from tkinter import *

from solution_brick import Brick


def binom(n, k):
	if 0 <= k <= n:
		ntok = 1
		ktok = 1
		for t in range(1, min(k, n - k) + 1):
			ntok *= n
			ktok *= t
			n -= 1
		return ntok // ktok
	else:
		return 0


def generator(lines):
	array = []
	for n in range(0, lines + 1):
		for k in range(0, n + 1):
			array.append(binom(n, k))

		yield array
		array = []


size = 10

master = Tk()
master.wm_title("pascalsche dreiecke".title())
cheight = (size + 1) * 51
cwidth = (size + 1) * 51
canvas = Canvas(master, height=cheight, width=cwidth, bg="white")
canvas.pack()

ausgabe = generator(size)
tempheight = 30
for row in ausgabe:
	print(row)
	tempwidth = (cwidth / 2) - ((len(row) - 1) * 50 / 2)
	for brick_text in row:
		Brick(canvas, brick_text, tempwidth, tempheight)
		tempwidth += 50
	tempheight += 50
mainloop()
