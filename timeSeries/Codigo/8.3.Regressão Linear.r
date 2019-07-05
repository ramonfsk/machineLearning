#Series temporais e analises preditivas - Fernando Amaral
library(forecast)
library(ggplot2)

plot(Seatbelts)
x1 = tslm(DriversKilled ~ trend, data=Seatbelts)
x2 = tslm(DriversKilled ~ season, data=Seatbelts)
x3 = tslm(DriversKilled ~ trend + season, data=Seatbelts)

CV(x1)
CV(x2)
CV(x3)

#fazendo previsao
r1 = forecast(x1,h=12)
r2 = forecast(x2,h=12)
r3 = forecast(x3,h=12)

autoplot(r1)
autoplot(r2)
autoplot(r3)

plot(r1)
lines(r2$mean, col="red")
lines(r3$mean, col="green")
legend("topright",legend=c("Tend","Seas","Tend + Seas"), col = c("blue","red","green"), lty=1:2, cex=0.8)