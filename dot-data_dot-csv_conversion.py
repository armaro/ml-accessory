import csv

with open('file.data') as input:
   lines = input.readlines()
   newLines = []
   for line in lines:
      newLine = line.strip().split()
      newLines.append( newLine )

with open('out.csv', 'w') as output:
   file = csv.writer(output)
   file.writerows( newLines )
