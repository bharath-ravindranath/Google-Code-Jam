from math import sqrt; from itertools import count, islice

def is_prime(number):
	return number > 1 and all(number%i for i in islice(count(2), int(sqrt(number)-1)))



def jamcoin(case):
    L = input().split(' ')
    N = int(L[0])
    J = int(L[1])

    number = 10**(N-1)+1
    print(number)
    count = 0
    not_jamcoin = 0
    
    print("Case #",case,":",sep='')
    while count != J:
    	for i in range(2,11):
    		if is_prime(int(str(number),i)):
    			not_jamcoin = 1
    			break
    	if not_jamcoin == 0:
    		count = count+1
    		print("Found a jamcoin:", number)

    	else:
    		not_jamcoin = 0
    	c = str(bin(int(str(number),2)+int('10',2)))
    	number = int(c[2:])
    	print(number)


    

    
T = int(input())
for i in range(1,T+1):
    jamcoin(i)

