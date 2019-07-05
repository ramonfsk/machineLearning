#Series temporais e analises preditivas - Fernando Amaral

library(ggplot2)
library(forecast)
library(seasonal)
library(seasonalview)

#sazonalidade e tendencia
plot(co2)
abline(reg=lm(co2~time(co2)))

#decomposicao classica
classicdecco2 = decompose(co2)
autoplot(classicdecco2)

#decomposicao classica
autoplot(fdeaths)
x = decompose(fdeaths)
autoplot(x)

#X-13ARIMA-SEATS
x13ap = seas(AirPassengers)
autoplot(x13ap)

#mstl
msap =   mstl(AirPassengers)
autoplot(msap)

#vizao grafica
view(x13ap)

ggseasonplot(AirPassengers)  
ggseasonplot(AirPassengers, polar = T)
ggmonthplot(AirPassengers)








