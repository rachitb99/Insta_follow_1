import os
import csv

# hdfsufgasfb
# user@2000

directory = 'accounts'

count={}

existing=[]

for filename in os.listdir(directory):
    existing.append(filename[:-14])
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
      with open(f, mode='r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
          if len(lines) > 1:
            if lines[1] in count:
              count[lines[1]] += 1
            else:
              count[lines[1]] = 1

count=[(x,y) for x,y in count.items()]

count.sort(key=lambda x: -x[1])

try:
  os.remove("output.csv")
except:
  pass
with open('output.csv', 'a') as ofile:
  for a, b in count:
    if a not in existing and a!="userName" and b>=3:
      ofile.write(a + '\n')
