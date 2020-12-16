import csv

def cria_csv(filename,res):
 csv_file = filename+".csv"
 csv_columns = res[0].keys()
 try:
     with open(csv_file, 'w') as csvfile:
         writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
         writer.writeheader()
         for data in res:
             writer.writerow(data)
 except IOError:
     print("I/O error: " + filename)
