from tkinter import *

import turtle  
pasos = turtle.Turtle() 
pasos.color("Purple")
pasos.speed(3)
  
for i in range(1): 

    #Primer cuadro
    pasos.forward(100) 
    pasos.left(90) 
    pasos.forward(100)
    pasos.left(90)
    pasos.forward(100) 
    pasos.left(90) 
    pasos.forward(100)
    pasos.left(90)
    
    
    # Segunda parte
    #PenUp para levantar el lápiz, PenDown para bajar el lápiz, 
    # Goto coordenadas para mover el lápiz a una posició
    pasos.penup()
    pasos.goto(50,50)
    pasos.pendown()

    #Repetimos el primer cuadro
    pasos.forward(100) 
    pasos.left(90) 
    pasos.forward(100)
    pasos.left(90)
    pasos.forward(100) 
    pasos.left(90) 
    pasos.forward(100)
    pasos.left(90)

    #Conectar vertices
    pasos.penup()
    pasos.goto(0,0)
    pasos.pendown()
    pasos.goto(50,50)
    pasos.penup()
    pasos.goto(100,0)
    pasos.pendown()
    pasos.goto(150,50)
    pasos.penup()
    pasos.goto(100,100)
    pasos.pendown()
    pasos.goto(150,150)
    pasos.penup()
    pasos.goto(0,100)
    pasos.pendown()
    pasos.goto(50,150)
    
turtle.done()