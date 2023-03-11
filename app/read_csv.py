import csv


def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    #Leer nombre de columnas
    header = next(reader)
    lists = []
    for row in reader:
      country_dic = dict(zip(header, row))
      lists.append(country_dic)
    return lists


if __name__ == '__main__':
  data = read_csv('./data.csv')
  print(data)
