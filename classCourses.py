import csv

def loadCourses():
  X = []
  Y = []

  file = open('busca.csv' 'r')
  readFile = csv.reader(file)
  next(readFile)

  for home,busca,logado,comprou in readFile:
    data = [
      int(home),
      str(busca),
      int(logado)
    ]
    X.append(data)
    Y.append(int(comprou))
    
  return X,Y