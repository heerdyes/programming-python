from turtle import *
import geom

ctr = 0
sqd = {}

while True:
  s = input('> ')
  lst = s.split()
  cmd = lst[0]
  if cmd == 'bye':
    break
  if cmd == 'square':
    amt = int(lst[1])
    sqid = 'sq_' + str(ctr)
    tmpsqr = geom.Square(pos(), amt)
    sqd[sqid] = tmpsqr
    print(sqid)
    tmpsqr.drawme()
    ctr = ctr + 1
  elif cmd == 'move':
    x1 = int(lst[1])
    y1 = int(lst[2])
    print(x1, y1)
    pu()
    goto(x1, y1)
    pd()
  elif cmd == 'sqdel':
    sqentry = sqd[lst[1]]
    print(sqentry)
    pu()
    goto(sqentry.xy)
    pd()
    color('white')
    sqentry.drawme()
    color('black')
  elif cmd == 'sqdir':
    print(sqd)
  elif cmd == 'resurrect':
    deadsqid = lst[1]
    deadsquare = sqd[deadsqid]
    print('resurrecting', deadsquare)
    pu()
    goto(deadsquare.xy)
    pd()
    sqr(deadsquare.s)

