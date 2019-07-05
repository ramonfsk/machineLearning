#Series temporais e analises preditivas - Fernando Amaral
library(forecast)
library(ggplot2)

autoplot(fdeaths)
#verifica a média
mean(fdeaths)
#previsao com metodo meanf
prev = meanf(fdeaths, h=5)
print(prev)
autoplot(prev)

#fazendo uma previsao com um subconjunto dos dados
fdeaths2 = window(fdeaths,start=c(1976,1),end=c(1979,12))
autoplot(fdeaths2)
mean(fdeaths2)
prev2 = meanf(fdeaths2, h=5)
print(prev2)
autoplot(prev2)

#compara as duas previsões
plot(prev)
lines(prev2$mean, col="red")



