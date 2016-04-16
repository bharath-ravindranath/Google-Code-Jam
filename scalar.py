
def scalar(case):
    value = int(input())
    n1 = [int(s) for s in input().split(" ")]
    n2 = [int(s) for s in input().split(" ")]
    n1.sort()
    n2.sort(reverse=True)
    ssum = 0;
    for i in range(value):
        ssum = ssum + n1[i]*n2[i]
    print("Case #", case, ": ",ssum, sep='')

T = int(input())
for i in range(1,T+1):
    scalar(i)

