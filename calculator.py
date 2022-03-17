#Calculator
from calcArt import logo

def add(n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2

def multply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1/n2

import os
def clear():
    os.system('clear')

operations = {
  "+":add,
  "-":subtract,
  "*":multply,
  "/":divide,
} 
def calculator():   
  print(logo)

  num1 = float(input("What is the first number?  "))


  for operation in operations:
    print(operation)
  shouldContinue = True
  while shouldContinue:
    oppSymbol = input("Pick an operation from the line above.  ")

    num2 = float(input("What is the next number?   "))

    calcFunction = operations[oppSymbol]
    answer = calcFunction(num1,num2)

    print(f"{num1} {oppSymbol} {num2} =    {answer}")


    stringTogether = input(f"Would you like to continue with {answer}(y) or start a new calculation(n)?  ")
    if stringTogether =="y":
      num1 = answer
    else:
      clear()
      calculator()

calculator()

