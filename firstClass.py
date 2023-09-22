class firstClass_1:
  
  def __init__(self, x1,y1,x2,y2,isVertical,isHorizontal,isRegular):
   self.x1 = x1
   self.y1 = y1
   self.x2 = x2
   self.y2 = y2
   self.isVertical = isVertical
   self.isHorizontal = isHorizontal
   self.isRegular = isRegular

  #determinants
  def Determ(col1, col2, col3):
    a1 = int(col1[0].get())
    a2 = int(col1[1].get())
    a3 = int(col1[2].get())
    b1 = int(col2[0].get())
    b2 = int(col2[1].get())
    b3 = int(col2[2].get())
    c1 = int(col3[0].get())
    c2 = int(col3[1].get())
    c3 = int(col3[2].get())
    
    return a1*((b2*c3)-(c2*b3)) - b1*((a2*c3)-(c2*a3)) + c1*((a2*b3)-(a3*b2))

