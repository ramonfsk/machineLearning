import pandas as pd
from collections import Counter
df = pd.read_csv('busca.csv')

X_df = df[['home', 'busca', 'logado']]
Y_df = df['comprou']

Xdummies_df = pd.get_dummies(X_df)
Ydummies_df = Y_df

X = Xdummies_df.values
Y = Ydummies_df.values

trainingPercent = 0.8
trainingPercentTest = 0.1

trainingSize = int(trainingPercent * len(Y))
trainingTestSize = int(trainingPercentTest * len(Y))
sizeValidation = len(Y) - trainingSize - trainingTestSize

# 0 a 799
trainingData = X[0:trainingSize]
trainingMarkings = Y[0:trainingSize]
# posicao final do array
endTest = trainingSize + trainingTestSize
# 800 a 899
testData = X[trainingTestSize:endTest]
testMarkings = Y[trainingTestSize:endTest]
# 900 a 999
dataValidate = X[endTest:]
markingValidate = Y[endTest:]

def fitAndPredict(name, model, trainingData, trainingMarkings, testData, testMarkings):
  model.fit(trainingData, trainingMarkings)

  result = model.predict(testData)
  hits = (result == testMarkings)
  #hits = [d for d in difference if d == 0]
  totalHits = sum(hits)
  totalElements = len(testData)
  taxHit = 100.0 * totalHits / totalElements
  msg = "Taxa de acerto do algoritmo {0}: {1}".format(name, taxHit)
  print(msg)
  return taxHit

def realTest(model, dataValidate, markingValidate):
  result = model.predict(dataValidate)
  hits = (result == markingValidate)

  totalHits = sum(hits)
  totalElements = len(markingValidate)

  taxHit = 100.0 * totalHits / totalElements

  msg = "Taxa de acerto do vencedor entre os dois algoritmos no mundo real: {0}".format(taxHit)
  print(msg)

from sklearn.naive_bayes import MultinomialNB
modelMultinomial = MultinomialNB()
resultMultinomial = fitAndPredict("MultinomialNB", modelMultinomial, trainingData, trainingMarkings, testData, testMarkings)

from sklearn.ensemble import AdaBoostClassifier
modelAdaBoost = AdaBoostClassifier()
resultAdaBoost = fitAndPredict("AdaBoostClassifier", modelAdaBoost, trainingData, trainingMarkings, testData, testMarkings)

if resultMultinomial > resultAdaBoost:
  winner = modelMultinomial
else:
  winner = modelAdaBoost

realTest(winner, dataValidate, markingValidate)

hitBase = max(Counter(testMarkings).values())
#oneHit = list(Y).count('sim')
#zeroHit = list(Y).count('nao')
baseTaxHit = 100.0 * hitBase / len(testMarkings)
print("Taxa de acerto base : %f" % baseTaxHit)

totalElements = len(dataValidate)
print("Total de teste: %d" % totalElements)