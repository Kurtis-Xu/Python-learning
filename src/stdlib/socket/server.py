import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen(5)  # 最大连接数
conn, addr = sk.accept()

print(conn)
print(addr)

while True:
    accept_data = conn.recv(1024)
    print('接收', accept_data.decode('utf-8'))
    conn.send('收到！'.encode('utf-8'))
