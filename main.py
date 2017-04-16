from tkinter import *


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


def generator(zeilen):
    array = []
    for n in range(0, zeilen + 1):
        for k in range(0, n + 1):
            array.append(binom(n, k))

        yield array
        array = []


master = Tk()
master.wm_title("pascalsche dreiecke".title())
cheight = 600
cwidth = 600
canvas = Canvas(master, height=cheight, width=cwidth, bg="white")

ausgabe = generator(10)
tempheight = 30
for row in ausgabe:
    print(row)
    tempwidth = (cwidth / 2) - ((len(row) - 1) * 50 / 2)
    for c_in_row in row:
        print(c_in_row)
        canvas.create_rectangle(tempwidth - 25, tempheight - 25, tempwidth + 25, tempheight + 25, fill="white")
        canvas.create_text(tempwidth, tempheight, text=c_in_row, font=("Century Gothic", 30))
        # TODO: ICH-hab-bock-auf-klassen
        # TODO: Ich auch
        tempwidth += 50
    tempheight += 50
canvas.pack()
mainloop()
