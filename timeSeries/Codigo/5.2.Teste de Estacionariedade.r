#Series temporais e analises preditivas - Fernando Amaral
library(urca)
library(forecast)

#teste de estacionariedade
x = ur.kpss(AirPassengers)
print(x)

#faz a diferenciacao
z = diff(AirPassengers)
#testa novamente
x = ur.kpss(z)
print(x)

split.screen( figs = c( 2, 1 ) )
screen(1)
plot(AirPassengers)
screen(2)
plot(z)
close.screen( all = TRUE )
