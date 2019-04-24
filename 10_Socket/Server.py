import socket

#  创建socket对象
s = socket.socket()

# 获取本地主机名
host = socket.gethostname()

print(host)

# 设置端口
port = 8090

# 绑定端口
s.bind((host, port))

# 等等客户端连接
s.listen(5)

try:
    while True:
        # 建立客户端连接
        sock, addr = s.accept()
        print('连接地址：', addr)
        data = sock.recv(1024)
        sock.send(data)
        sock.close()
finally:
    s.close()

