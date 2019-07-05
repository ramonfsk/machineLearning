#Series temporais e analises preditivas - Fernando Amaral

tempts = read.csv(file.choose(), sep=",",header = F)
print(tempts)
tempts = ts(tempts[2],start = 1884, end=1939, frequency=1)
class(tempts)
plot(tempts)



