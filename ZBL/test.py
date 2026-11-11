with open("ZBL/test.txt", "w") as f:
  f.write("\n")
  f.write("Now the file has more content!")
  f.write("\n")
  f.write("New line")

#open and read the file after the appending:
with open("ZBL/test.txt") as f:
  print(f.read())


