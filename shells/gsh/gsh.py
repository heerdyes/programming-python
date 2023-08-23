from turtle import *
import geom

ctr = 0
sqd = {}
cmds = []

def dosquare():
  global ctr
  print(lst)
  amt = int(lst[1])
  sqid = 'sq_' + str(ctr)
  tmpsqr = geom.Square(pos(), amt)
  sqd[sqid] = tmpsqr
  print(sqid)
  tmpsqr.drawme()
  ctr = ctr + 1

def domove():
  x1 = int(lst[1])
  y1 = int(lst[2])
  print(x1, y1)
  pu()
  goto(x1, y1)
  pd()

def dosqdel():
  sqentry = sqd[lst[1]]
  print(sqentry)
  pu()
  goto(sqentry.xy)
  pd()
  color('white')
  sqentry.drawme()
  color('black')

def doresurrect():
  deadsqid = lst[1]
  deadsquare = sqd[deadsqid]
  print('resurrecting', deadsquare)
  pu()
  goto(deadsquare.xy)
  pd()
  sqr(deadsquare.s)

def dosave():
  print('saving to file ' + lst[1])
  with open(lst[1], 'w') as f:
    f.write('\n'.join(cmds))

while True:
  s = input('> ')
  if s.startswith('save '):
    pass
  else:
    cmds.append(s)
  lst = s.split()
  cmd = lst[0]
  if cmd == 'bye':
    break
  if cmd == 'square':
    dosquare()
  elif cmd == 'move':
    domove()
  elif cmd == 'sqdel':
    dosqdel()
  elif cmd == 'sqdir':
    print(sqd)
  elif cmd == 'resurrect':
    doresurrect()
  elif cmd == 'save':
    dosave()

