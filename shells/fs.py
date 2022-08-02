def mkfile(cmdlst):
    param1 = cmdlst[1]
    fp = open(param1, 'w')
    fp.close()
    print('[cf] file created')

def wrfile(cmdlst):
    param1 = cmdlst[1]
    param2 = cmdlst[2]
    fp = open(param1, 'w')
    fp.write(param2)
    fp.close()
    print('[wf] file written')

def rffile(cmdlst):
    param1 = cmdlst[1]
    fp = open(param1, 'r')
    lns = fp.readlines()
    for ln in lns:
        print(ln, end='')
    fp.close()
