"""
CSV to Parallel Arrays (Lists)

Hannah
23/09/20

Reads the names and scores from CSV and asks the user for a  cut off score.They then print a comment for each person, whether they have passed or failed.
"""

names = []
scores = []

cut_off = int(input("Please enter the cut off score: "))

file  = open('data_in.csv')

for line in file:
  data = line.replace('"','').strip().split(',')

  names.append(data[0])
  scores.append(int(data[1]))
  

file.close()

for x in range(6):
  score = int(scores[x])
  name = names[x]

 

  if score >= cut_off:
  
    print("You have passed:")  
    print(name)
    print(score)

  if score < cut_off:
    print("You need to study more: ")
    print(name)
    print(score)