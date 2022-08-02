import datetime
import subprocess
import os
import fs
import sys

vardict = {}
if len(sys.argv) == 2:
    print('processing batch file: ' + sys.argv[1])
    bfp = open(sys.argv[1])
    batchlns = bfp.readlines()
    bfp.close()

ctr = 0
while True:
    if len(sys.argv) == 1:
        cmd = input('-> ')
    else:
        cmd = batchlns[ctr]
        ctr=ctr+1
    cmdlst = cmd.split()
        
    if cmdlst[0] in ['exit','q','quit']:
        break
    elif cmdlst[0] == 'hw':
        print('hello world')
    elif cmdlst[0] == 'date':
        print(datetime.datetime.now())
    elif cmdlst[0] == 'np':
        subprocess.call(['notepad.exe'])
    elif cmdlst[0] in ['help','h']:
        print('supported commands are: hw, date, np, help')
    elif cmdlst[0] == 'md':
        param1 = cmdlst[1]
        os.mkdir(param1)
    elif cmdlst[0] == 'cf':
        fs.mkfile(cmdlst)
    elif cmdlst[0] == 'wf':
        fs.wrfile(cmdlst)
    elif cmdlst[0] == 'rf':
        fs.rffile(cmdlst)
    elif cmdlst[0] == 'mkvar':
        vardict[cmdlst[1]] = cmdlst[2]
    elif cmdlst[0] == 'vars':
        for k in vardict.keys():
            print('-| %s -> %s' % (k,vardict[k]))
    else:
        print('cannot understand command: '+cmdlst[0])

print('goodbye!')
