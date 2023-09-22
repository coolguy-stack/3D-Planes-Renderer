import matplotlib.pyplot as plt
import numpy as np
from firstClass import firstClass_1 

temp = firstClass_1
temp.isVertical = False
from tkinter import*

root = Tk()
root.title = ("Lines")

# find z, cz + d = 0, z = -d/c
def Point(a,b,c,d):
  return [0, 0, -d/c]

#checks if it is linearly dependant or not
def lD(row1, row2):
  arr = []
  for row in arr:
      arr.append(row/row1[0])
  arr2 = []
  for row in row2:
      arr2.append(row/row2[0])
  
  for index in [0,1,2,3]:
      if arr[index] != arr2[index]:
          return False
  return True

#checks if it has 0/infinite solutions
def noSol(row1, row2, row3):

  if lD(row1, row2):
      return False
  if lD(row1, row3):
      return False
  if lD(row2, row3):
      return False
  return True

#action after "process" button is clicked
def button_click():
  xx, yy = np.meshgrid(range(50), range(50))

  #calculate the solution
  D = temp.Determ([a1, a2, a3], [b1, b2, b3], [c1, c2, c3])
  Dx = temp.Determ([d1, d2, d3], [b1, b2, b3], [c1, c2, c3])
  Dy = temp.Determ([a1, a2, a3], [d1, d2, d3], [c1, c2, c3])
  Dz = temp.Determ([a1, a2, a3], [b1, b2, b3], [d1, d2, d3])

  #if D = 0
  if D == 0:
    row1 = [int(a1.get()), int(b1.get()), int(c1.get()), int(d1.get())]
    row2 = [int(a2.get()), int(b2.get()), int(c2.get()), int(d2.get())]
    row3 = [int(a3.get()), int(b3.get()), int(c3.get()), int(d3.get())]
    if noSol(row1, row2, row3):
      typeOfLine.insert(0, "No Solutions. ")
    else:
      typeOfLine.insert(0, "Undefined. ")
      
  #else continue the program 
  else:
    sol_x = Dx/-D
    sol_y = Dy/-D
    sol_z = Dz/-D

  typeOfLine.insert(0, "The solution is x = "+str(sol_x)+", y = "+str(sol_y)+", z = "+str(sol_z))

  #plot first plane
  point = Point(
    int(a1.get()), int(b1.get()), int(c1.get()), int(d1.get()))
  point = np.array(point)
  normal = [int(a1.get()), int(b1.get()), int(c1.get())]
  normal = np.array(normal)
  d = -point.dot(normal)
  zz1 = (-normal[0] * xx - normal[1] * yy - d) * 1. / normal[2]

  #plot second plane
  point = Point(
    int(a2.get()), int(b2.get()), int(c2.get()), int(d2.get()))
  normal = [int(a2.get()), int(b2.get()), int(c2.get())]
  zz2 = (-normal[0] * xx - normal[1] * yy - d) * 1. / normal[2]

  #plot third plane
  point = Point(
    int(a3.get()), int(b3.get()), int(c3.get()), int(d3.get()))
  normal = [int(a3.get()), int(b3.get()), int(c3.get())]
  zz3 = (-normal[0] * xx - normal[1] * yy - d) * 1. / normal[2]

  # test plot
  fig = plt.figure()
  p = fig.add_subplot(111,projection='3d')
  p.plot_surface(xx, yy, zz1)
  p.plot_surface(xx, yy, zz2)
  p.plot_surface(xx, yy, zz3)
  plt.show()

#pull data from first X field
def enteredVal():
    return

# entry field creation
a1 = Entry(root, width=5, borderwidth=5, command=enteredVal())
labelA1 = Label(root, text="X + ")
b1 = Entry(root, width=5, borderwidth=5)
labelB1 = Label(root, text="Y + ")
c1 = Entry(root, width=5, borderwidth=5)
labelC1 = Label(root, text="Z + ")
d1 = Entry(root, width=5, borderwidth=5)
labelD1 = Label(root, text=" = 0")

a2 = Entry(root, width=5, borderwidth=5, command=enteredVal())
labelA2 = Label(root, text="X + ")
b2 = Entry(root, width=5, borderwidth=5)
labelB2 = Label(root, text="Y + ")
c2 = Entry(root, width=5, borderwidth=5)
labelC2 = Label(root, text="Z + ")
d2 = Entry(root, width=5, borderwidth=5)
labelD2 = Label(root, text=" = 0")

a3 = Entry(root, width=5, borderwidth=5, command=enteredVal())
labelA3 = Label(root, text="X + ")
b3 = Entry(root, width=5, borderwidth=5)
labelB3 = Label(root, text="Y + ")
c3 = Entry(root, width=5, borderwidth=5)
labelC3 = Label(root, text="Z + ")
d3 = Entry(root, width=5, borderwidth=5)
labelD3 = Label(root, text=" = 0")

#output field
typeOfLine = Entry(
    root,
    width=45,
    borderwidth=5,
)

#entry field placement
a1.grid(row=0, column=0)
labelA1.grid(row=0, column=1, padx=1, pady=1)
b1.grid(row=0, column=2, padx=1, pady=1)
labelB1.grid(row=0, column=3, padx=1, pady=1)
c1.grid(row=0, column=4, padx=1, pady=1)
labelC1.grid(row=0, column=5, padx=1, pady=1)
d1.grid(row=0, column=6, padx=1, pady=1)
labelD1.grid(row=0, column=7, padx=1, pady=1)

a2.grid(row=1, column=0)
labelA2.grid(row=1, column=1, padx=1, pady=1)
b2.grid(row=1, column=2, padx=1, pady=1)
labelB2.grid(row=1, column=3, padx=1, pady=1)
c2.grid(row=1, column=4, padx=1, pady=1)
labelC2.grid(row=1, column=5, padx=1, pady=1)
d2.grid(row=1, column=6, padx=1, pady=1)
labelD2.grid(row=1, column=7, padx=1, pady=1)

a3.grid(row=2, column=0)
labelA3.grid(row=2, column=1, padx=1, pady=1)
b3.grid(row=2, column=2, padx=1, pady=1)
labelB3.grid(row=2, column=3, padx=1, pady=1)
c3.grid(row=2, column=4, padx=1, pady=1)
labelC3.grid(row=2, column=5, padx=1, pady=1)
d3.grid(row=2, column=6, padx=1, pady=1)
labelD3.grid(row=2, column=7, padx=1, pady=1)

#output field placement
typeOfLine.grid(row=5, column=1, columnspan=8, padx=8, pady=8)

a1.insert(0, "a1")
b1.insert(0, "b1")
c1.insert(0, "c1")
d1.insert(0, "d1")

a2.insert(0, "a2")
b2.insert(0, "b2")
c2.insert(0, "c2")
d2.insert(0, "d2")

a3.insert(0, "a3")
b3.insert(0, "b3")
c3.insert(0, "c3")
d3.insert(0, "d3")


button_1 = Button(root,
                  text="process",
                  padx="10",
                  pady="10",
                  command=button_click) 
button_1.grid(row=5, column=0)
root.mainloop()
