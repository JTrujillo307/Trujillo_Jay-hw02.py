#Name: Jay Trujillo
#Lab Section: 15
#Submission Date: 11/12/24
#Sources, help given to/received from
#Jhett Carr


lines = []
use = []
with open("promt.txt") as file, open("out2.txt","w") as newfiles:
  for lines in file:
    line = lines.replace("/t" , " ").split(" ")
    tem = " "
