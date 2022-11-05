try:
    num=input('enter something')
    sym=input('symiiii---->')
    print(f'count={num.count(sym)}')
except Exception as ex:
    print(f'erorr information:{ex}')