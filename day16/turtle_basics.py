from turtle import Turtle, Screen

timmy= Turtle() #creating an object of Turtle Class
timmy.shape("turtle")
timmy.color("violet") #body colour
timmy.pencolor("brown")  #body outline
timmy.forward(100) # make the turtle move 100 spaces


my_screen = Screen() #the window where our turtle will be visible
print(my_screen.canvheight)
my_screen.exitonclick()  #exiting on click


