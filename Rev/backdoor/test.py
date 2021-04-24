import marshal, dis

f = open("bd.pyc", "rb")
f.seek(16) # Skip 16 byte header (for Python 3.8)
co = marshal.load(f)
print(dis.dis(co))
