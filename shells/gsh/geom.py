from turtle import *

class Square:
  def __init__(t, xy, sz):
    t.s = sz
    t.xy = xy
    print('square:', t.xy, t.s)
    
  def __str__(t):
    return "Square at %s, size: %d" % (t.xy, t.s)
    
  def drawme(t):
    for i in range(4):
      fd(t.s)
      lt(90)

