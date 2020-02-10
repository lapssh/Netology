def main():
    #global x
    global n
    print (n)
    x = 0
    while x <= n:
        function_1()
        function_2()
def function_1():
    global x
    x += 1
    print(x)

def function_2():
    global x
    x += 1
    print(x)


n = 10
x = 0
main()