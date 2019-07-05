#Series temporais e analises preditivas - Fernando Amaral
library(forecast)
library(ggplot2)

modelo = auto.arima(co2, trace = T)
print(modelo)

modelo2 = auto.arima(co2, trace = T,stepwise = F, approximation = F )
print(modelo2)

prev1 = forecast(modelo,h=12)
plot(prev1)

prev2 = forecast(modelo2,h=12)
plot(prev2)

print(prev1$mean)
print(prev2$mean)

plot(prev1)
lines(prev2$mean, col="red")


