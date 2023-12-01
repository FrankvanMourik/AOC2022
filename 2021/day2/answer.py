def result1():
    h=0
    d=0
    for b in open('data/data.txt'):
        if b[0]=="d":
            d+=int(b[-2])
        elif b[0]=="u":
            d-=int(b[-2])
        else:
            h+=int(b[-2])
    print(h*d)


def result2():
    h,d,a=0,0,0
    for b in open('data/data.txt'):
        if b[0] == "d":
            a += int(b[-2])
        elif b[0] == "u":
            a -= int(b[-2])
        else:
            h += int(b[-2])
            d += int(b[-2])*a
    print(h * d)

def result2_golf():
    h=d=a=0
    for b in open('d'):
        x=int(b[-2])
        if b[0]=="d":a+=x
        if b[0]=="u":a-=x
        if b[0]=="f":h+=x;d+=x*a
    print(h*d)


if __name__ == "__main__":
    result2_golf()