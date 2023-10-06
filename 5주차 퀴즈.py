def ggdan(n):
    for x in range(1,n+1):
        print("------[" + str(x) + "단] ------")
        for y in range(1,x+1):
            print(x, "X", y, "=", x*y)
print("----------------")

num = int(input("몇 단까지 출력할까요?"))
ggdan(num)


