import csv

def loadAccess():
    #os arays de nome data e markings foram substituídos por X e Y
    X = []
    Y = []

    file = open('acesso.csv', 'r')
    readerFile = csv.reader(file)
    next(readerFile)

    for home, como_funciona, contato, comprou in readerFile:
        data = [
            int(home),
            int(como_funciona),
            int(contato)
        ]
        X.append(data)
        Y.append(int(comprou))

    return X, Y