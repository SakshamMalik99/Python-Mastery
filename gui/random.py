import random
p1=0
p2=0
p3=0
for i in range(20):
    x = random.randrange(1,7)
    p1=p1+x
print("\n")
for i in range(20):
    x = random.randrange(1,7)
    p2=p2+x
print("\n")
for i in range(20):
    x = random.randrange(1,7)
    p3=p3+x
print("P1: ",p1)
print("P2: ",p2)
print("P3: ",p3)
if p1>p2 and p1>p3:
    print("Win P1")
elif p2>p1 and p2>p3:
    print("Win P2")
else:
    print("Win P3")
