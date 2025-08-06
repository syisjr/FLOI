import random
import uuid
for i in range(1,11):
    with open(f"E:\\programming\\c++\\我的\\题目编写\\第一届FLOI\\easy\\Mark\\test{i}.in","w",encoding="utf-16") as intext:
        n=random.randint(1,1001)
        m=random.randint(1,n+1)
        k=random.randint(1,int(1e18+1))
        intext.write(f"{n} {m} {k}\n")
        for t in range(n):
            intext.write(chr(random.randint(0,25)+ord('a')))
            intext.write(uuid.uuid4().hex[1:10])
            intext.write(" ")
        intext.write("\n")
        summ=0
        for t in range(n):
            x=random.randint(1,int(1e18+1))
            while(summ+x>int(1e18)):
                x=random.randint(1,int(1e18+1))
            intext.write(str(x))
            intext.write(" ")
        intext.write("\n") 