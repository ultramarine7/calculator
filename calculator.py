"""Calculator
Prompt the user to select a shape, Depending on the shape the user selects, 
calculate the area of that shape, Print the area of that shape to the user"""
from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

raw_input("The calculator is booting up.")

print "Current time is {}/{}/{} {}:{}".format (now.month, now.day, now.year, now.hour, now.minute)

sleep(1)

hint = "Don't forget to include the correct units! \nExiting..."

option = raw_input ("Enter C for Circle or T for Triangle: ")
option = option.upper()

if option == "C":
  radius = float(raw_input("Enter radius: "))
  area = pi * radius ** 2
  print "The pie is baking..."
  sleep(1)
  print "Area: %.2f. %s" % (area,hint)
elif option == "T":
  base = float(raw_input("Enter the base of the Triangle: "))
  height = float(raw_input("Enter the height of the Triangle: "))
  area = base * height * (0.5)
  print "Uni Bi Tri..."
  sleep(1)
  print "Area: %.2f. %s" % (area,hint)
else:
  print "Error! Invalid shape selector specified. Exiting."