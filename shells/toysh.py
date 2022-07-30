import os
import sys
from exc import *
from sh import process_line, process_batch

vardict = {}

try:
    if len(sys.argv) == 2:
        cmdfile=sys.argv[1]
        if not cmdfile.endswith('.toy'):
            raise NotAToyException()
        with open(cmdfile, 'r') as cfp:
            clns = [x.rstrip() for x in cfp.readlines()]
        process_batch(clns, vardict)
    elif len(sys.argv) == 1:
        while True:
            cmd = input('toy-> ')
            try:
                process_line(cmd, vardict)
            except ContinueSignal as cs:
                continue
            except BreakSignal as bs:
                break
    else:
        print('unsupported number of arguments: %d'%len(sys.argv))
        print('exiting.')
except NotAToyException as nate:
    print('you passed a file that is not a toy!')
    print('exiting.')

