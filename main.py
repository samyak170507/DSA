n = int(input())

for i in range(n):

    req, curr, price = map(int, input().split())

    temp = req-curr

    if temp <0 : 
        print(req*price)

    else:
        print(temp*price)

