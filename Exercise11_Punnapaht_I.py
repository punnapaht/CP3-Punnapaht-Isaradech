number = int(input("NUMBER : "))
for x in range(number):
    y = ""*(number-x)
    z = "*"*(x*2+1)
    print(y,z)
