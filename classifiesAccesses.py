from dados import loadAccess
X,Y = loadAccess()

from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(X, Y)

print(model.predict([[1,0,1], [0,1,0], [1,0,0], [1,1,0], [1,1,1]]))

result = model.predict(X)
difference = result - Y
hits = [d for d in difference if d == 0]
totalHits = len(hits)
totalElements = len(X)
taxHit = 100.00 * totalHits / totalElements

print(taxHit)
print(totalElements)