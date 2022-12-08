n = int(input("Enter the number: "))
x = 0
y = 1
for i in range(1,n+1):
    nxt = x+y
    x = y
    y = nxt
    print(nxt)
