#Series temporais e analises preditivas - Fernando Amaral
library(forecast)
library(ggplot2)

#lambda = 0, logaritmica 
t1 = BoxCox(AirPassengers,lambda =0 )
autoplot(t1)

#lambda = 0.34 
t2 = BoxCox(AirPassengers,lambda =.1 )
autoplot(t2)

#gera labda automático
lbd = BoxCox.lambda(AirPassengers)
print(lbd)
t3 = BoxCox(AirPassengers,lambda =lbd )
autoplot(t3)

#diferenciacao 
t4 = diff(AirPassengers)
autoplot(t4)

#logaritmica
t5 = log10(AirPassengers)
autoplot(t5)

split.screen( figs = c( 2, 2 ) )
screen(1)
plot(t1)
screen(2)
plot(t2)
screen(3)
plot(t3)
screen(4)
plot(t5)
close.screen( all = TRUE )




