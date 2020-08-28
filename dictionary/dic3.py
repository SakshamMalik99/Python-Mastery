port = {22: "SSH", 23: "Telnet" , 53: "DNS", 80: "HTTP" }
print(port)
print(port[23])
port[23]="DATA 1"
print(port)
del port[22]
print(port)
