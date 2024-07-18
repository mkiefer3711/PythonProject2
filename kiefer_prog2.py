# MovingTurtle.py - Move a circular turtle left-to-right across the screen

# Import the turtle package
import turtle


# Function for drawing a turtle at current position
def draw_turtle(ttl):
    
    # To fill the color in star
    ttl.fillcolor('green') 
    
    
    # Start color filling
    ttl.begin_fill()
    
    # Draw a square but commented out
    #ttl.forward(50)
    #ttl.left(90)
    #ttl.forward(50)
    #ttl.left(90)
    #ttl.forward(50)
    #ttl.left(90)
    #ttl.forward(50)
    #ttl.left(90)
   
   # Draw a Star
    for i in range(5):
 
        # moving turtle 100 units forward
        ttl.forward(100)
 
        # rotating turtle 144 degree right
        ttl.right(144)
    
    # End color filling
    ttl.end_fill()
    
    # Outline color
    ttl.pencolor("yellow")
    
    # Outline thickness
    ttl.pensize(3)
    

# Define a function to draw the title
def draw_title(the_title):
    
    # Create a turtle for drawing the title
    ttl = turtle.Turtle()
    
    # Lift the pen
    ttl.penup()
    
    # Move the pen to the initial writing location
    ttl.setpos(-240, 160)
    
    # Set the pen color 
    ttl.color('lightblue')
    
    # Set the font, size, and style
    style = ('Arial', 16, 'italic')
    
    # Write the text on the screen
    ttl.write(the_title, font=style)
    
    # Hide the turtle so it no longer displays the cursor
    ttl.hideturtle()


# The while loop will continue so long as Running is True
Running = True


# Define a stop function that will set Running to False
def stop(a, b):
    
    # Global so that the outer Running is set
    global Running
    Running = False

Background_Color=input("Please choose a background color: ")

# Create a screen object
screen = turtle.Screen()

# Set the screen size
screen.setup(500, 400)

# Set the screen background color
screen.bgcolor(Background_Color)

# Screen updates set for animation
screen.tracer(0)

# Capture left mouse click; call 'stop' when click occurs
screen.onclick(stop)

# Call function to display the title
draw_title('Maddison Kiefer')

# Create a turtle object. We'll call it 'sam'
sam = turtle.Turtle()

# Set the turtle color
sam.color('blue')

# Set the turtle speed
sam.speed(2) 

# Hide the turtle
sam.hideturtle()          

# Lift the turtle pen
sam.penup()               

# Set sam's initial position
sam.goto(0, 100) 

# Drop turtle pen to surface
sam.pendown()             

# Infinite loop; but stops on left mouse click
# This is the code that does the animation
while Running :
    
    # Clear turtle at current position
    sam.clear()  
    
    # Call function to draw the turtle
    draw_turtle(sam)
    
    # Update the screen
    screen.update()    
    
    # Move turtle forward a tiny amount
    sam.forward(0.025)
    
    # Move turtle right a tiny amount
    sam.right(0.015)

# We get here after the user clicks the left mouse button
# Terminate the program
exit()
