import sys
def my_print(*args,sep=" ",end="\n",file=sys.stdout):
    a=sep.join(str(i) for i in args)+end
    sys.stdout.write(str(a))
