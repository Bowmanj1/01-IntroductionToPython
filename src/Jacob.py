import rosegraphics as rg
window = rg.TurtleWindow
turtle2 = rg.SimpleTurtle()
turtle2.pen = rg.Pen('red', 4)
turtle2.speed = 30
for k in range(10):
    for k in range(15):
        for k in range(3):
            turtle2.draw_circle(k ** k)
            turtle2.forward(10 * k)
        turtle2.left((180/15) * k)
    turtle2.pen_up()
    turtle2.forward((10 - k) ** 2)
    turtle2.pen_down()
window.close_on_mouse_click()
for k in range(5):
    for k in range(15):
        turtle2.draw_circle(100)
        turtle2.left(24)
    turtle2.forward(k)
