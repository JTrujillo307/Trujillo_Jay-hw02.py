#Name: Jay Trujillo
#Lab Section: 15
#Submission Date: 11/12/24
#Sources, help given to/received from
#Jhett Carr


lines = []
use = []
with open("promt.txt") as file, open("out2.txt","w") as newfiles:
  for lines in file:
    line = lines.replace("\t" , " ").split(" ")
    tem = ""
    for key in line:
      use = key.split(":")
      if(len(use)== "w"):
        if(use[0]== "w"):
          tem += (" "*int(use[1]))
        else:
          tem +=("*"*int(use[1]))
    newfile.write(tem + "\n")
