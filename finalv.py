import turtle

# Initialize the turtle
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("white")
t = turtle.Turtle()
t.penup()
t.hideturtle()
t.speed(3)

# Function to draw a pattern of dots
def draw_dot_grid(dot_spacing, levels):
    for row in range(-levels, levels + 1):  # Loop through rows
        num_dots = levels - abs(row)  # Calculate the number of dots in this row
        for col in range(-num_dots, num_dots + 1):  # Loop through columns
            x = col * dot_spacing
            y = row * dot_spacing
            t.goto(x, y)  # Move the turtle to the dot position
            t.dot(10, "black")  # Draw a black dot

# Function to draw an arc with a fixed radius of 30 and a specified center
def draw_arc(radius=25, extent=270, center=(0, 0), reverse=False,mk=0):
    # Move the turtle to the starting point of the arc
    # t.goto(center[0] + radius, center[1])  # Move to the starting position (radius away from the center)
    t.setheading(mk)  #start where it want to move first Set the angle to point upwards to start drawing the arc
    
    # Draw the arc using the specified center point
    if reverse:
        t.circle(-radius, extent)  # Reverse arc (clockwise)
    else:
        t.circle(radius, extent)  # Normal arc (counterclockwise)

draw_dot_grid(60, 3)

# Start drawing the pattern
t.penup()

# Move directly to starting point (0, 150) without drawing a line
t.goto(0, 150)

# Start drawing a line to (-165, -15)
t.pendown()
t.goto(-165, -15)

# Draw an arc from (-165, -15) to (-165, 15) with a radius of 30 (75% circle)
draw_arc(radius=25, extent=270, center=(-180, 0), reverse=True,mk=220)

# Move from (-165, 15) to (-150, 0)
t.goto(-150, 0)

t.goto(0,-150)
t.goto(15,-165)
draw_arc(radius=25,extent=270,center=(0,-180),reverse=True,mk=310)
t.goto(0,-150)


t.goto(150,0)
t.goto(165,15)

draw_arc(radius=25,extent=270,center=(180,0),reverse=True,mk=45)

t.goto(150,0)

t.goto(0,150)
t.goto(-15,165)
draw_arc(radius=25,extent=270,center=(0,180),reverse=True,mk=140)

t.goto(0,150)


# one plan 
t.penup()
t.goto(-45,15)
t.pendown()

t.goto(-105,75)
draw_arc(radius=22,extent=180,center=(-120,60),reverse=False,mk=130)
t.goto(-135,45)
t.goto(-105,15)

draw_arc(radius=22,extent=100,center=(-105,0),reverse=True,mk=-45)
t.goto(-105,-15)

t.goto(-135,-45)
draw_arc(radius=22,extent=180,center=(-120,-60),reverse=False,mk=230)
t.goto(-105,-75)
t.goto(-45,-15)

draw_arc(radius=22,extent=100,center=(-45,0),reverse=False,mk=45)
t.goto(-45,15)


# two plan 
# Right side mirrored pattern
t.penup()
t.goto(45, 15)
t.pendown()

t.goto(105, 75)
draw_arc(radius=22, extent=180, center=(120, 60), reverse=True, mk=45)  # Reverse direction
t.goto(135, 45)
t.goto(105, 15)

draw_arc(radius=22, extent=100, center=(105, 0), reverse=False, mk=225)  # Reverse direction
t.goto(105, -15)

t.goto(135, -45)
draw_arc(radius=22, extent=180, center=(120, -60), reverse=True, mk=-45)  # Reverse direction
t.goto(105, -75)
t.goto(45, -15)

draw_arc(radius=22, extent=100, center=(45, 0), reverse=True, mk=-225)  # Reverse direction
t.goto(45, 15)

# three plan up side plan 
t.penup()
t.goto(-15, -45)
t.pendown()

t.goto(-75,-105 )
draw_arc(radius=22, extent=180, center=(-60,-120), reverse=False, mk=240)  # Reverse direction

t.goto(-45, -135)
t.goto(-15,-105 )

draw_arc(radius=22, extent=100, center=(0,-105), reverse=True, mk=45)  # Reverse direction
t.goto(15, -105)

t.goto(45, -135)
draw_arc(radius=22, extent=180, center=(60, -120), reverse=False, mk=310)  # Reverse direction
t.goto(75, -105)
t.goto(15, -45)

draw_arc(radius=22, extent=100, center=(0, -45), reverse=False, mk=135)  # Reverse direction
t.goto(-15,-45 )


# Four Plan Mirrored Upside
t.penup()
t.goto(-15, 45)  # Mirrored starting point
t.pendown()

t.goto(-75, 105)  # Mirrored movement
draw_arc(radius=22, extent=180, center=(-60, 120), reverse=True, mk=120)  # Mirrored arc direction

t.goto(-45, 135)
t.goto(-15, 105)

draw_arc(radius=22, extent=100, center=(0, 105), reverse=False, mk=-45)  # Mirrored arc direction
t.goto(15, 105)

t.goto(45, 135)
draw_arc(radius=22, extent=180, center=(60, 120), reverse=True, mk=45)  # Mirrored arc direction
t.goto(75, 105)
t.goto(15, 45)

draw_arc(radius=22, extent=100, center=(0, 45), reverse=True, mk=225)  # Mirrored arc direction
t.goto(-15, 45)



# final thing 

# Start the drawing
# Line from (-15, 75) to (-75, 15)
t.penup()
t.goto(-15, 75)
t.pendown()
t.goto(-75, 15)

# Arc from (-75, 15) to (-75, -15)
draw_arc(radius=22, extent=100, center=(-75, 0), reverse=False, mk=225)

# Line from (-75, -15) to (-15, -75)
t.goto(-75, -15)

t.goto(-15,-75)
# Arc from (-15, -75) to (15, -75)
draw_arc(radius=22, extent=100, center=(0, -60), reverse=False, mk=320)

# Line from (15, -75) to (75, -45)
t.goto(75, -15)

# Arc from (75, -45) to (75, 45)
draw_arc(radius=22, extent=100, center=(60, 0), reverse=False, mk=45)

# Line from (75, 45) to (15, 75)
t.goto(15, 75)

# Arc from (15, 75) to (-15, 75)
draw_arc(radius=22, extent=100, center=(0, 60), reverse=False, mk=135)


# New modification: Move to (-180, 0) and draw the arc with 75% circle
# t.goto(-180, 0)  # Move to the new starting point (-180, 0)
# draw_arc(radius=30, extent=270, center=(-180, 0), reverse=True)  # Draw arc in reverse (clockwise)

# # Move from (-150, 0) to (-150, 0) (back to the same point)
# t.goto(-150, 0)

# Complete the pattern
t.penup()

# Keep the window open
screen.mainloop()
