from game2dboard import Board
from algo import solve
import star


def mouse_fn(btn, row, col):  # mouse calback function
    b[row][col] = 1 if not b[row][col] else 0


b = Board(3, 4)  # 3 rows, 4 columns, filled w/ None
b[0][0] = 1
b.title = "Click me!"
b.cell_size = 120
b.cell_color = "bisque"
b.on_mouse_click = mouse_fn
# b.show()


# solve([5, 6, 2, 4, 7, 8, 1, 3, None], [1, 2, 3, 4, 5, 6, 7, 8, None], delay=0.05)
star.solve("021", "120")

print("Done.")
