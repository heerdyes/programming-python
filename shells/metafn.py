def fn1():
    print('this is fn1')
    
def fn2():
    print('this is fn2')
    
usrfn = input('enter function name: ')

# going to magically call it now
vars()[usrfn]()

