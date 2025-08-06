for i in range(1,11):
    with open(f"e:\\programming\\c++\\我的\\题目编写\\第一届FLOI\\easy\\总伤害\\test{i}.in","r",encoding="utf-16") as f:
        n,k=map(int,f.readline().split())
        l=list(map(int,f.readline().split()))
        with open(f"e:\\programming\\c++\\我的\\题目编写\\第一届FLOI\\easy\\总伤害\\test{i}.out","w",encoding="utf-16") as o:
            o.write(str(sum(l)*k))