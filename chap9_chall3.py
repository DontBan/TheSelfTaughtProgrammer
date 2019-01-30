import csv

list1 = ['Top Gun', 'Risky Business', 'Minority Report']
list2 = ['Titanic', 'The Revenant', 'Inception']
list3 = ['Training Day', 'Man on Fire', 'Flight']

with open('movies.csv', 'w', newline='') as f:
    w = csv.writer(f, delimiter=',')
    w.writerow(list1)
    w.writerow(list2)
    w.writerow(list3)
