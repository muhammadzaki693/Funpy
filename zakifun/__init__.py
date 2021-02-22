import termcolor
from termcolor import colored

def create():
  print("created")

def template(select):
  if select == "hello world":
    print("hello world")
  elif select == "calculator":
    while 1:
      x = int(input("type a number: "))
      z = int(input("type an number: "))
      y = input("select: ")
      
      if y == "+":
        print(x+z)
      elif y == "-":
        print(x-z)
      elif y == "×":
        print(x*z)
      elif y == "^":
        print(x**z)
      else:
        print(colored("uknown: "+y, "red"))
        break
  else:
    print(colored("selectError: undefine", "red"))