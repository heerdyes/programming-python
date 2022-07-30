from exc import *
import fs
import datetime
import subprocess

def process_batch(clns, vardict):
    for cln in clns:
        try:
            process_line(cln, vardict)
        except ContinueSignal as cs:
            continue
        except BreakSignal as bs:
            break

def process_line(cmd, vardict):
    cmdlst = cmd.split()
    # handle special cases
    if len(cmdlst) == 0:
        raise ContinueSignal()
    
    if cmdlst[0] in ['exit','q','quit']:
        raise BreakSignal()
    
    # regular handling
    if cmdlst[0] == 'hw':
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
        fs.rdfile(cmdlst)
    elif cmdlst[0] == 'mkvar':
        vardict[cmdlst[1]] = cmdlst[2]
    elif cmdlst[0] == 'vars':
        for k in vardict.keys():
            print('-| %s -> %s' % (k,vardict[k]))
    elif cmdlst[0] == 'p':
        print(' '.join(cmdlst[1:]))
    else:
        print('cannot understand command: '+cmdlst[0])

