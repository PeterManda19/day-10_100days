import time
print("Welcome to the split bill calculator!")
time.sleep(2)
print()
while True:
  try:
    myBill = float(input("What was the bill?: "))
    print()
  except ValueError:
    print()
    print("I am expecting positive numbers.")
    print()
    continue
  if myBill < 0:
    print()
    print("Bill cannot be negative.")
    print()
    continue
  else:
    break
    
while True: 
  try:
    tipPerc = float(input("What percentage of tip will you leave to be added to the bill total? "))
    print()
  except ValueError:
    print()
    print("I am expecting numbers.")
    print()
    continue  
  if tipPerc < 0:
    print()
    print("Tip percentage cannot be negative")
    print()
    continue
  else:
    break
    
while True:   
  try:
    numberOfPeople = int(input("How many people?: "))
    print()
  except ValueError:
    print()
    print("We count people using whole numbers or integers.")
    print("Please, enter a valid integer")
    print()
    continue  
  if numberOfPeople <= 0:
    print()
    print("Are you a ghost?")
    print('There has to be atleast one person to pay the bill.')
    print()
    continue  
  else:  
    break
  
totalBill = myBill + (myBill *(tipPerc/100))
answer = float(totalBill / numberOfPeople)
answer = "{0:.2f}".format(answer)  
print("You all owe", answer)
print()
print("Thank you.")

while True:
  input()
  print()
  print("To use the calculator again please click stop on top right of console and run again.")
  print("Thank you.")