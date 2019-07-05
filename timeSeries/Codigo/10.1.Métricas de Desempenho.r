#Series temporais e analises preditivas - Fernando Amaral
library(forecast)
library(ggplot2)

treino = window(fdeaths, start=c(1974,1), end=c(1977,12))
teste = window(fdeaths, start=c(1978,1), end=c(1979,12))

#regressão
modelo1 = tslm(treino ~ season + trend, data=treino)
prev1 = forecast(modelo1, h=24)
autoplot(prev1)

#rnn
modelo2 = nnetar(treino)
prev2 = forecast(modelo2, h=24)
autoplot(prev2)

plot(fdeaths)
lines(prev1$mean, col="blue")
lines(prev2$mean, col="red")
lines(teste, col="green")
legend("topright",legend=c("Reg.","Rn","Teste"), col = c("blue","red","green"), lty=1:2, cex=0.8)

accuracy(prev1,teste )
accuracy(prev2,teste )






