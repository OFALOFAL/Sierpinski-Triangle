import tkinter as tk

Tk = tk.Tk()

WIDTH = 600
HEIGHT = 380

canvas = tk.Canvas(Tk, width=WIDTH, height=HEIGHT, bg='black', bd=0, highlightthickness=0)

canvas.pack()


def midpoint(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (x1+x2)/2, (y1+y2)/2


def sierpinski(depth, A, B, C):
    if depth == 0:
        return
    for x in range(3 ** depth):
        mid_ab = midpoint(A, B)
        mid_ac = midpoint(A, C)
        mid_bc = midpoint(B, C)
        mid_points = [*mid_ab, *mid_ac, *mid_bc]
        canvas.create_polygon(mid_points, fill='black')
        sierpinski(depth - 1, A, mid_ab, mid_ac)
        sierpinski(depth - 1, mid_ab, B, mid_bc)
        sierpinski(depth - 1, mid_ac, mid_bc, C)


length = WIDTH
A = [WIDTH / 2, 0]
B = [WIDTH, HEIGHT]
C = [0, HEIGHT]
canvas.create_polygon([A, B, C], fill='white')
sierpinski(4, A, B, C)

tk.mainloop()
