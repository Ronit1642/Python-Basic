import csv
data =[
		['Name', 'Age'],
		['Amal', 35],
		['Bimal', 45],
		['Kamal', 55]
	       ]   

with open("E:\\efgh.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
with open('E:\\efgh.csv', newline='') as csvfile:
           data = csv.reader(csvfile, delimiter=' ')
           for row in data:
               print(', '.join(row))


