import turtle as trtl

class TurtlePattern:
    shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic",
              "arrow", "turtle", "circle", "square", "triangle", "classic",
              "arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle"]
    
    colors = ["red", "blue", "green", "orange", "purple", "gold",
              "red", "blue", "green", "orange", "purple", "gold",
              "red", "blue", "green", "orange", "purple", "gold", "red", "blue"]
    
    shape_color_map = {"arrow": "red",
                       "turtle": "blue",
                       "circle": "green",
                       "square": "orange",
                       "triangle": "purple", 
                       "classic": "gold"}
    
    def __init__(self, shape, color, x_pos, y_pos, angle, step_size):  
        self.t = trtl.Turtle(shape=shape)
        self.t.speed(0)
        self.t.penup()
        self.t.color(color)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.angle = angle
        self.step_size = step_size
    
    def draw(self):
        self.t.goto(self.x_pos, self.y_pos)
        self.t.pendown()
        self.t.setheading(self.angle)
        self.t.forward(self.step_size)

        self.x_pos = self.t.xcor()   
        self.y_pos = self.t.ycor()
        self.angle = self.t.heading()
    
    def __str__(self):
        return (f"Shape: {self.t.shape()}, "
                f"Color: {self.t.color()[0]}, "
                f"Available Shapes: {', '.join(self.shapes)}, "
                f"Available Colors: {', '.join(self.colors)}")

if __name__ == "__main__":
    turtle_list = []

x_pos = 0
y_pos = 0
angle = 180
step_size = 45

for i in range(len(TurtlePattern.shapes)):
    current_shape = TurtlePattern.shapes[i]
    current_color = TurtlePattern.colors.pop(0)
    turtle_obj = TurtlePattern(current_shape, current_color, x_pos, y_pos, angle, step_size)
    turtle_obj.draw()
    turtle_list.append(turtle_obj)

    x_pos = turtle_obj.t.xcor()
    y_pos = turtle_obj.t.ycor()
    angle += 45
    step_size += 15

    print(turtle_obj)

wn = trtl.Screen()
wn.mainloop()
