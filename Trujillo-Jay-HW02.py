# Jay Trujillo
# UWYO COSC 1010
# Submission Date: 10/29/24
# HW 02
# Lab Section: 15
# Sources, people worked with, help given to: 
# Kaleb Moler

Dictionary = { "A":".-" , "B": "-..." , "C":"-.-." , "D":"-.." , "E":"." , "F":"..-." , "G":"--." , "H":"...." , "I":".." , "J":"---" , "K":"-.-" , "L":".-.." , "M":"--" , "N":"-." , "O":"---" , "P":".--." , "Q":"--.-" , "R":".-." , "S":"..." , "T":"-" , "U":"..-" , "V":"...-" , "W":".--" , "X":"-..-" , "Y":"-.--" , "Z":"--.." } 

message = input("What would you like to ake into morse code?")
message = message.upper()
for char in message:
  if char in Dictionary:
    print(Dictionary[char], end=" ")
