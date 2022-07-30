def mkfile():
    param1 = cmdlst[1]
    fp = open(param1, 'w')
    fp.close()
    print('[cf] file created')

def wrfile():
    param1 = cmdlst[1]
    param2 = cmdlst[2]
    fp = open(param1, 'w')
    fp.write(param2)
    fp.close()
    print('[wf] file written')
