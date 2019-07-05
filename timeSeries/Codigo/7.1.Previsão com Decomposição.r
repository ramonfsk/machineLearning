#Series temporais e analises preditivas - Fernando Amaral

library(forecast)
library(ggplot2)

autoplot(AirPassengers)
previ = stlf(AirPassengers, h=48)
print(previ)
autoplot(previ)



