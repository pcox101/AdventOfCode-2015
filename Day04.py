import hashlib

i = 0
while True:
    s = 'ckczppom' + str(i)
    h = hashlib.md5(s.encode()).hexdigest()
    if h.startswith("00000"):
        break
    i = i + 1
    
print ("Part 1: " + str(i))

i = 0
while True:
    s = 'ckczppom' + str(i)
    h = hashlib.md5(s.encode()).hexdigest()
    if h.startswith("000000"):
        break
    i = i + 1
    
print ("Part 2: " + str(i))