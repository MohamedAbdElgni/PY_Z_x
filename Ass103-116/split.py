x = (input())
s = set(map(int, input().split()))
counter = int(input())
while counter > 0:

    op = input().split()
    if len(op[0]) < 4:
        eval("s."+op[0]+"()")
        counter -= 1
    else:
        eval("s."+op[0]+f"({int(op[1])})")
        counter -= 1
