def f1(**kwargs):
    if 'end' in kwargs:
        endF1 = kwargs['end']
    else:
        endF1 = "\n"
    for key, value in kwargs.items():
        print(key, value, end=endF1)
f1(par1=1, par2=2, par3=3, par4=4, par5=5, end="fdfdfdfsdf")
