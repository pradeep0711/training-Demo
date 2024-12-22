def grad(n,na,mc,mj):
    print(f"Number : {n}")
    print(f"Name : {na}")
    avg = mc+mj
    print(avg)
    if avg > 90:
        print("A")
    elif avg < 80:
        print("B")
    elif avg > 50 and avg < 60:
        print("C")
    else:
        print("Fail")
n1 = int(input())
n2 = str(input())
mc1 = int(input())
mj1 = int(input())
grad(n1,n2,mc1,mj1)
