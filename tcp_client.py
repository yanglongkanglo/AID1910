"""
tcp_client.py  tcp客户端
"""

from socket import *

# 创建tcp套接字
sockfd = socket()  # 默认参数--》 tcp

# 连接服务器
server_addr = ('127.0.0.1',8888) # 服务端地址
sockfd.connect(server_addr)

while True:
    data = input("Msg>>")
    if not data:
        break
    # 发送给服务端
    sockfd.send(data.encode()) # 转换为字节串
    # if data == '##':
    #     break
    data = sockfd.recv(1024)
    print("Server:",data.decode()) # 打印字符串

# 关闭套接字
sockfd.close()






