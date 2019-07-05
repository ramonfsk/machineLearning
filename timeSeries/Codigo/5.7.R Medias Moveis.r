#Series temporais e analises preditivas - Fernando Amaral
library(forecast)
library(ggplot2)

autoplot(fdeaths)

#calculando a media movel com ordem 5
fdeaths2 = ma(fdeaths, order = 5 )
autoplot(fdeaths2)

#novamente, ordem 12
fdeaths3 = ma(fdeaths,order=12)
autoplot(fdeaths3)

#limpeza dos dados
fdeaths4 = tsclean(fdeaths)
autoplot(fdeaths4)

#comparando 
plot(fdeaths)
lines(fdeaths2, col="red")
lines(fdeaths3, col="blue")
lines(fdeaths4, col="green")

#legenda
legend("topright",legend=c("Orig.","Ma5","Ma12","Tsc"), col = c("black","red","blue","green"), lty=1:2, cex=0.8,)









