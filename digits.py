from math import sqrt
def digits(case):
    n = int(input())
    three_digit = int(pow(3+sqrt(5),n))%1000
    print("Case #",case,": ",str(three_digit).zfill(3),sep='')
        

T = int(input())
for i in range(1,T+1):
    digits(i)


