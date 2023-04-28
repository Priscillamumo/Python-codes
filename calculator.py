def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))

def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))

print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")
print("e. Exit")

choice = input("input your choice: ")

if choice == "A":
    print("Addition")
    a = int(input("Input your first number: "))
    b = int(input("input your second number: "))
    add(a, b)
elif choice == "B":
    print("Subtraction")
    a = int(input("Input your first number: "))
    b = int(input("input your second number: "))
    sub(a, b)
elif choice == "C":
    print("Multiplication")
    a = int(input("Input your first number: "))
    b = int(input("input your second number: "))
    mul(a, b)
elif choice == "D":
    print("Division")
    a = int(input("Input your first number: "))
    b = int(input("input your second number: "))
    div(a, b)
elif choice == "E":
    print("Exit")

quit()

