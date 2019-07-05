#Series temporais e analises preditivas - Fernando Amaral

library(forecast)
library(ggplot2)

plot(Seatbelts)

#olhamos apenas uma variavel
autoplot( Seatbelts[, c("DriversKilled")])

#criamos um subconjunto
cintos = window(Seatbelts[, c("DriversKilled")], start=c(1980,1), end=c(1983,12))

#criamos modelo arrima normal
modelo1 = auto.arima(cintos)
modelo1

prev1= forecast(modelo1, h=12)
print(prev1)
autoplot(prev1)

#separa motoristas para o modelo
motoristas =   as.vector(window(Seatbelts[, c("drivers")], start=c(1980,1), end=c(1983,12)))
motoristas
#novo modelo arima
modelo2 = auto.arima(cintos, xreg = motoristas   )
modelo2

#previsao
motoristas2 =   as.vector(window(Seatbelts[, c("drivers")], start=c(1984,1), end=c(1984,12)))
prev2 = forecast(modelo2, xreg = motoristas2)
print(prev2)
autoplot(prev2)

plot(prev1)
lines(prev2$mean, col="red")


