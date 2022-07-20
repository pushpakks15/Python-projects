#Calculator
def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2

calculate={
  "+":add,
  "-":divide,
  "*":multiply,
  "/":divide,
}
def calculator():
  num1=float(input("Enter first number: "))
  num2=float(input("Enter second number: "))
  
  for operation in calculate:
    print(operation)
  symbol=input("Enter the operation to be performed")
  solve=calculate[symbol](num1,num2)
  print(f"{num1} {symbol} {num2} = {solve}")
  other_operation=True
  while other_operation:
    other_operation=input("Do you want to continue: yes or no? or you can also start a new calculation by typing 'new'.")
    if other_operation=="no":
      other_operation=False
      print("Thank you for using the calculator")
    elif other_operation=="yes":
      symbol2=input(f"Enter the operation to be performed on {solve} ")
      num3=float(input("Enter the third number: "))
      answer=calculate[symbol2](solve,num3)
      print(f"{solve} {symbol2} {num3} = {answer}")
      solve=calculate["*"](answer,1)
    elif other_operation=="new":
      calculator()

calculator()









     
