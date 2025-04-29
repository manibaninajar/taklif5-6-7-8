#get input
a = input("fist number: ")
b = input("second number: ")
op = input("oprator (+ - * //): ")

a = int(a)
b = int(b)

if op == "+":
        print("result: ", a+b)
elif op == "-":
        print("result: ", a-b)
elif op == "*":
        print("result: " , a*b)
elif op == "/":
    if b == 0:
        print("error ! cannot divide by zero.")
else :
    print("result: " , a//b )