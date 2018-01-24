#This program is an exercise of using turtle module in python to draw several shapes

import turtle

#draw a square
#@param: turtle instance
def draw_square(my_turtle):
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
  
#draw a circle   
#@param: turtle instance
def draw_circle(my_turtle):
    my_turtle.circle(100)

#draw a triangle
#@param: turtle instance    
def draw_triangle(my_turtle):
    my_turtle.forward(100)
    my_turtle.right(120)
    my_turtle.forward(100)
    my_turtle.right(120)
    my_turtle.forward(100)
    my_turtle.right(120)

#draw some art
#@param: turtle instance 
def draw_art1(my_turtle):
    for i in range(36):
        draw_square(my_turtle)
        my_turtle.right(10)

#draw some art
#@param: turtle instance 
def draw_art2(my_turtle):
    for i in range(36):
        my_turtle.forward(50)
        my_turtle.right(45)
        my_turtle.forward(50)
        my_turtle.right(135)
        my_turtle.forward(50)
        my_turtle.right(45)
        my_turtle.forward(50)
        my_turtle.right(135)
        
        my_turtle.right(10)
    
    my_turtle.right(90) 
    my_turtle.forward(200)   
        
window=turtle.Screen() #create a graphics window
window.bgcolor("black")

toto=turtle.Turtle() #create a turtle
toto.shape("turtle")
toto.color("green")

angie=turtle.Turtle() #create a turtle
angie.shape("turtle")
angie.color("blue")

adam=turtle.Turtle() #create a turtle
adam.shape("turtle")
adam.color("white")

adam.speed(9)
draw_art2(adam)
#draw_square(adam)
#draw_circle(angie)
#draw_triangle(toto)

window.exitonclick()
