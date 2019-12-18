"""
epoll_server.py tcp服务
重点代码

思路: poll()返回
"""
from socket import *
from select import *

# 创建监听套接字，作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)

# 创建poll对象
p = poll()
# 建立查找字典
fdmap = {s.fileno(): s}
# 关注s套接字
p.register(s, POLLIN)

# 循环监控IO发生
while True:
    # 提交监控
    events = p.poll()
    for fd, event in events:
        if fd == s.fileno():
            c, addr = s.accept()
            print('Connect from', addr)
            p.register(c, POLLIN | POLLERR)  # 添加新的关注IO
            fdmap[c.fileno()] = c
        else:
            data = fdmap[fd].recv(1024).decode()

