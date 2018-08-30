import rosegraphics as rg
window = rg.TurtleWindow
turtle2 = rg.SimpleTurtle()
turtle2.pen = rg.Pen('red', 12)
turtle2.speed = 1
turtle2.right(72)

for k in range(5):
    turtle2.forward(200)
    turtle2.right(144)

window.close_on_mouse_click()