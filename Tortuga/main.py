from tkinter import *

import turtle  
pasos = turtle.Turtle() 
  
for i in range(1): 
    #Primer cuadro
    pasos.forward(100) 
    pasos.right(90) 
    pasos.forward(100)
    pasos.right(90)
    pasos.forward(100) 
    pasos.right(90) 
    pasos.forward(100)
    pasos.left(90)
    pasos.forward(0) 
    # Segunda parte
    pasos.left(45) 
    pasos.forward(50)
    pasos.left(90)
    pasos.forward(100) 
    pasos.left(90) 
    pasos.forward(100)
    pasos.left(90)
    pasos.forward(100) 
    pasos.left(90) 
    pasos.forward(100)
    pasos.left(90)
    
turtle.done()