#define the funcions
def add(a, b):
 answer = a + b
 print(str(a) + "+" + str(b) + "=" + str(answer))

def sub(a, b):
 answer = a - b
 print(str(a) + "-" + str(b) + "=" + str(answer))

def mul(a, b):
 answer = a * b
 print(str(a) + "*" + str(b) + "=" + str(answer))

def div(a, b):
 answer = a / b
 print(str(a) + "/" + str(b) + "=" + str(answer))

while True:
 print("A. addition")
 print("B. substraction")
 print("C. multiplication")
 print("D. division")
 print("Exit")

 choice = input("Input your choice: ")
 if choice == "a" or choice == "A":
  print("Addition")
  a = int(input("Input first number: "))
  b = int(input("Input second number: "))
  add(a, b)
 elif choice == "b" or choice =="B":
  print("Substration")
  a = int(input("Input first number: "))
  b = int(input("Input second number: "))
  sub(a, b)
 elif choice == "c" or choice =="C":
  print("Multiplication")
  a = int(input("Input first number: "))
  b = int(input("Input second number: "))
  mul(a, b)
 elif choice == "d" or choice =="D":
  print("Division")
  a = int(input("Input first number: "))
  b = int(input("Input second number: "))
  div(a, b)
 elif choice == "e" or choice == "E":
  print("Program ended")
  quit()
