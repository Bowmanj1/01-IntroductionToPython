"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Jacob Bowman.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg

window = rg.TurtleWindow

size1 = 200
turtle1 = rg.SimpleTurtle('turtle')
turtle1.pen = rg.Pen('green', 2)
turtle1.speed = 10

for k in range(18):
    turtle1.draw_circle(size1)
    turtle1.pen_up()
    turtle1.backward(10)
    turtle1.pen_down()
    size1 = size1 - 10

turtle2 = rg.SimpleTurtle()
turtle2.pen = rg.Pen('red', 12)
turtle2.speed = 3
turtle2.right(72)

for k in range(5):
    turtle2.forward(100)
    turtle2.right(144)

window.close_on_mouse_click()