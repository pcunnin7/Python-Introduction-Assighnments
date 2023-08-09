line = "Reply from 216.58.192.206: bytes=32 time=30ms TTL=115"
total = 5


ms = line.find("ms")
time = line.find("time=")
ping = line[time+5:ms]
total += int(ping)



print(total)
