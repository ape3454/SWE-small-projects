from shapes import Paper, Triangle, Rectangle, Oval

paper = Paper()

rect1 = Rectangle()

rect1.set_width(200)
rect1.set_height(100)
rect1.set_x(700)
rect1.set_y(400)
rect1.set_color("OrangeRed3")

rect1.draw()

tri1 = Triangle()
tri1.x = 800
tri1.y = 350
tri1.x2 = 660
tri1.y2 = 401
tri1.x3 = 940
tri1.y3 = 401

# if you can't see the triangle, maximise the window and scroll.

tri1.draw()

paper.display()

#Source: Raspberry Pi Foundation is licensed under CC-BY-SA 4.0.