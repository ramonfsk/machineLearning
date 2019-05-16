from dados import loadAccess
X,Y = loadAccess()
# a abordagem utilizada foi separar os dados para treino e teste em proporação 90/10
#a taxa foi de 88.89%
trainingData = X[:90]
trainingMarkings = Y[:90]

testData = X[-9:]
testMarkings = Y[-9:]

from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(trainingData, trainingMarkings)

print(model.predict([[1,0,1], [0,1,0], [1,0,0], [1,1,0], [1,1,1]]))

result = model.predict(testData)
difference = result - testMarkings
hits = [d for d in difference if d == 0]
totalHits = len(hits)
totalElements = len(testData)
taxHit = 100.0 * totalHits / totalElements

print(taxHit)
print(totalElements)