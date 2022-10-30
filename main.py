import time
print("Welcome to the split bill calculator!")
time.sleep(2)
print()
while True:
  myBill = input("What was the bill?: ")
  print()
  if myBill.isnumeric() == True:
    myBill = float(myBill)  
    break
  else:
    continue
    
while True: 
  tipPerc = input("What percentage of tip will you leave to be added to the bill total? ")
  print()
  if tipPerc.isnumeric() == True:
    tipPerc = float(tipPerc)
    break
  else:
    continue
    
while True:   
  try:
    numberOfPeople = int(input("How many people?: "))
    print()
  except ValueError:
    print("We count people using whole numbers or integers.")
    print("Please, enter a valid integer")
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