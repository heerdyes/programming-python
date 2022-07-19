import datetime
import subprocess

while True:
    cmd = input('-> ')
    if cmd in ['exit','q','quit']:
        break
    elif cmd == 'hw':
        print('hello world')
    elif cmd == 'date':
        print(datetime.datetime.now())
    elif cmd == 'np':
        subprocess.call(['notepad.exe'])
    elif cmd in ['help','h']:
        print('supported commands are: hw, date, np, help')
    else:
        print('cannot understand command: '+cmd)
    

print('goodbye!')
