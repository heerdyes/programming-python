import datetime
import subprocess
import os

vardict = {}

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

while True:
    cmd = input('-> ')
    cmdlst = cmd.split()
    # ['cf', 'abc.txt']
    
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
        mkfile()
    elif cmdlst[0] == 'wf':
        wrfile()
    elif cmdlst[0] == 'mkvar':
        vardict[cmdlst[1]] = cmdlst[2]
    elif cmdlst[0] == 'vars':
        for k in vardict.keys():
            print('-| %s -> %s' % (k,vardict[k]))
    else:
        print('cannot understand command: '+cmdlst[0])

print('goodbye!')
