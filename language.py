import re
L = input().split(' ')
dic = []
for i in range(0,int(L[1])):
    dic.append(str(input()))
print(dic)
for i in range(0,int(L[2])):
    line = str(input())
    list1 = []
    while '(' in line:
        list1.append(line[line.find("(")+1:line.find(")")])
        line = line[line.find(")")+1:]
    print(list1)
	    
