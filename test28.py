# -*- coding: UTF-8 -*-

# Filename : test28.py
# author by : STT

import socket
import sys
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#获取本地主机名
host=socket.gethostname()

port=9999

#连接服务
s.connect((host,port))

#接收小于1024字节的数据
msg=s.recv(1024)

s.close()

print(msg.decode('utf-8'))
#绑定端口
#serversocket.bind(host,port)

#设置最大连接数，超过后排队
#serversocket.listen(5)

#while True:
    #建立客户端连接
 #   clientsocket,addr=serversocket.accept()
#
  #  print('连接地址： %s '% str(addr))
#
  #  msg='欢迎访问菜鸟教程！' + '\r\n'
  #  clientsocket.send(msg.encode('utf-8'))
  #  clientsocket.close()
