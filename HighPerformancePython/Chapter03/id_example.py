import dis

def funcA():
    a = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,40,50,60,70,80,90,100,110,[1,2])
    print(f"funcA id(a): {id(a)}")
    print(f"funcA id(a[-1]): {id(a[-1])}")
    print(f"funcA id(a[-1][0]): {id(a[-1][0])}")
    b = 50000
    print(f"funcA id(b): {id(b)}")


def funcB():
    a = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,40,50,60,70,80,90,100,110,[1,2])
    print(f"funcB id(a): {id(a)}")
    print(f"funcA id(a[-1]): {id(a[-1])}")
    b = 50000
    print(f"funcA id(b): {id(b)}")


if __name__ == '__main__':
    funcA()
    funcB()
    a = {}
    a["AAA"] = "111"
    a["AAA"] = "222"
    print(f"{a['AAA']}")
