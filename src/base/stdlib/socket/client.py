import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

while True:
    send_data = input('输入：')
    sk.send(send_data.encode('utf-8'))
    accept_data = sk.recv(1024)  # 每次接收多大的字节包
    print('响应', accept_data.decode('utf-8'))
