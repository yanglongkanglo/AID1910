"""
select 函数示例
"""
from select import select
from socket import *
from time import sleep

s = socket()
s.bind(('127.0.0.1',8888))
s.listen(3)

f = open('file','r')

print("IO监控")
sleep(5)
rs,ws,xs = select([s,f],[],[])
print("rlist:",rs)
print("wlist:",ws)
print("xlist:",xs)

