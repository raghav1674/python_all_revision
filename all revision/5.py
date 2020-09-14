import argparse
parser=argparse.ArgumentParser()
parser.add_argument("number1",help="frstnumber")
parser.add_argument("operation",help="operation",\
                    choices=["square"])
arg=parser.parse_args()
n1=int(arg.number1)
result=None
if arg.operation=="square":
    result=n1**2

print(result)

import sys

arg=sys.argv
print(arg[1])