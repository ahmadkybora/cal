def sum(a, b):
    result = a+b
    print(f"a+b = {result}")

def sub(a, b):
    result = a-b
    print(f"a-b = {result}")

def mul(a, b):
    result = a*b
    print(f"a*b = {result}")

def div(a, b):
    result = a/b
    print(f"a/b = {result}")

a = int(input("adad aval"))
b = int(input("adad dovom"))

operator = input("amalgar")

if operator == "+":
    sum(a, b)
elif operator == "-":
    sub(a, b)
elif operator == "*":
    mul(a, b)
elif operator == "/":
    div(a, b)
else:
    print("amalgar eshtebah ast")
