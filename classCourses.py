import pandas as pd
from collections import Counter
df = pd.read_csv('busca.csv')

X_df = df[['home', 'busca', 'logado']]
Y_df = df['comprou']

Xdummies_df = pd.get_dummies(X_df)
Ydummies_df = Y_df

X = Xdummies_df.values
Y = Ydummies_df.values

trainingPercent = 0.9
trainingSize = int(trainingPercent * len(Y))
trainingTestSize = len(Y) - trainingSize

trainingData = X[:trainingSize]
trainingMarkings = Y[:trainingSize]

testData = X[-trainingTestSize:]
testMarkings = Y[-trainingTestSize:]

from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(trainingData, trainingMarkings)

result = model.predict(testData)
hits = (result == testMarkings)
#hits = [d for d in difference if d == 0]
totalHits = sum(hits)
totalElements = len(testData)
taxHit = 100.0 * totalHits / totalElements

print("Taxa de acerto do algoritmo: %f" % taxHit)
print(totalElements)

#a eficiencia do algoritmo que chuta tudo em um unico valor
hitBase = max(Counter(testMarkings).values())
#oneHit = list(Y).count('sim')
#zeroHit = list(Y).count('nao')
baseTaxHit = 100.0 * hitBase / len(testMarkings)
print("Taxa de acerto base : %f" % baseTaxHit)